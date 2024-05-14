from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from src.content_generator import ContentGenerator
from src.exec import send_mail


app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
content_generator = ContentGenerator()


app.secret_key = b'\xcf\x15V\xa1\x04\x8d\xe3\xd7\x84\xe5\x8c\xd0\x10\xf8\xb8\xe7\xec7\x8f\xea\xa7\xee\xf1\x80\xddm\xcb\xe7'
app.config['SESSION_TYPE'] = 'filesystem'



# @app.route('/')
# def login():
#     return render_template('/login1/index.php')

@app.route('/')
def index():
    return render_template('Main.html')

@app.route("/jobs_stud", methods=['GET'])
def jobs_stud():
    return render_template("Jobs_stud.html")

@app.route("/our_team", methods=['GET'])
def our_team():
    return render_template("OurTeam.html")

@app.route("/interview", methods=['GET'])
def interviewer():
    # job_description = request.json.get('job_description')
    # title = request.json.get('title')
    # role = request.json.get('role')

    # Process the received parameters as needed
    # For example, you can pass them to a template
    # return redirect(f"/InterviewBot.html?job_description={job_description}&title={title}&role={role}")
    # return render_template("InterviewBot.html", job_description=job_description, title=title, role=role)
    return render_template("InterviewBot.html")

chat_history = []
dict1 = {}

@app.route('/interview-runner', methods=['POST'])
def interview_runner():
    session['current_question_index'] = session.get('current_question_index', 0)
    
    flag = request.json.get('flag')

    if request.method == 'POST' and flag == '1':
        job_description = request.json.get('job_description', '')

        if job_description:
            flag, emotion, question = content_generator.interview_question(job_description, session['current_question_index'])
            session['current_question_index'] += 1

            print(f"--->\n-->Session: {session['current_question_index']}\n-->Flag: {flag}\n-->Emotion: {emotion}\n-->Question: {question}\n--->")
            dict1['question'] = question
            return jsonify({'question': question}), 200
        

    if request.method == 'POST' and flag == '0':
        answer = request.json.get('answer', '')
        job_description = request.json.get('job_description', '')

        if answer:
            score = content_generator.score_answer('', answer)
            dict1['answer'] = answer
            dict1['score'] = score
            chat_history.append(dict1)
            print(f"--->\n-->Score: {score}")

        if job_description:
            flag, emotion, question = content_generator.interview_question(job_description, session['current_question_index'])
            session['current_question_index'] += 1
            score = round(score, 1)
            print(f"\n-->Session: {session['current_question_index']}\n-->Flag: {flag}\n-->Emotion: {emotion}\n-->Question: {question}\n--->")

            if flag == -1:
                session.pop('current_question_index', None)
                question = "The interview has ended."

                report = content_generator.get_report(chat_history)
                if not chat_history:
                    return jsonify({'question': question, "flag": flag}), 200
                send_mail("k213218@nu.edu.pk", report)

                return jsonify({'question': question, "flag": flag}), 200

            dict1['question'] = question
            return jsonify({'question': question, "flag": flag, "score": score}), 200 


    if request.method == 'POST' and flag == '-1':
        session.pop('current_question_index', None)

        question = "Stop Button pressed, The interview has ended."

        report = content_generator.get_report(chat_history)
        if not chat_history:
            return jsonify({'question': question}), 200
        send_mail("k213218@nu.edu.pk", report)

        return jsonify({'question': question}), 200

    return jsonify({'error': 'Invalid request'}), 400



if __name__ == '__main__':
    app.run(debug=True)
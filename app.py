from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.content_generator import ContentGenerator

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
content_generator = ContentGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hr')
def hr_portal():
    return render_template('hr_portal.html')

@app.route('/students')
def student_interviews():
    return render_template('student_interviews.html')


@app.route('/generate-interview-question', methods=['POST'])
def generate_interview_question():
    global current_question_index

    if request.method == 'POST':
        job_description = request.json.get('job_description', '')

        if job_description:
            emotion, question = content_generator.interview_question(job_description, current_question_index)
            
            current_question_index += 1

            return jsonify({"emotion": emotion, 'question': question}), 200

    return jsonify({'error': 'Invalid request'}), 400

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    if request.method == 'POST':
        answer = request.json.get('answer', '')
        emotion = request.json.get('emotion', '')

        if answer:
            score = content_generator.score_answer(emotion, answer)
            return jsonify({'score': score}), 200

    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)

// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch interview questions from the backend
    function fetchInterviewQuestion() {
        fetch('/generate-interview-question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                job_description: 'Sample job description' // Replace with actual job description
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display the interview question on the page
            document.getElementById('interviewQuestion').innerText = data.question;
            // You can also handle displaying emotion if needed
            document.getElementById('emotion').innerText = data.emotion;
        })
        .catch(error => console.error('Error:', error));
    }

    // Function to submit answer to the backend
    function submitAnswer(answer, emotion) {
        fetch('/submit-answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                answer: answer,
                emotion: emotion
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display the score on the page
            document.getElementById('score').innerText = 'Score: ' + data.score;
        })
        .catch(error => console.error('Error:', error));
    }

    // Event listener for fetching interview questions
    document.getElementById('fetchQuestionBtn').addEventListener('click', function () {
        fetchInterviewQuestion();
    });

    // Event listener for submitting answers
    document.getElementById('submitAnswerBtn').addEventListener('click', function () {
        const answer = document.getElementById('answerInput').value;
        const emotion = document.getElementById('emotion').innerText; // Assuming emotion is displayed on the page
        submitAnswer(answer, emotion);
    });
});

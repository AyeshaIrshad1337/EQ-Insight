document.addEventListener('DOMContentLoaded', function() {
    // Handle job posting form submissions
    const addJobForm = document.getElementById('addJobForm');
    if (addJobForm) {
        addJobForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const jobDescription = document.getElementById('jobDescription').value;
            fetch('/jobs', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({description: jobDescription})
            })
            .then(response => response.json())
            .then(data => {
                alert('Job added!');
                document.getElementById('jobDescription').value = ''; // Clear the input after submit
                fetchJobs(); // Refresh the list of jobs
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Fetch and display jobs
    fetchJobs();

    // Handle answer submissions
    const submitAnswerButton = document.getElementById('submitAnswer');
    if (submitAnswerButton) {
        submitAnswerButton.addEventListener('click', function() {
            const answer = document.getElementById('answerBox').value;
            const emotion = document.getElementById('emotionHolder').value; // Assuming you store the current emotion somewhere
            fetch('/submit-answer', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({answer: answer, emotion: emotion})
            })
            .then(response => response.json())
            .then(data => {
                alert('Score: ' + data.score);
                document.getElementById('answerBox').value = ''; // Clear the textarea after submitting
                fetchQuestion(); // Fetch the next question
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Fetch the next interview question
    const fetchQuestionButton = document.getElementById('fetchQuestion');
    if (fetchQuestionButton) {
        fetchQuestionButton.addEventListener('click', function() {
            fetchQuestion();
        });
    }
});

function fetchJobs() {
    fetch('/jobs')
    .then(response => response.json())
    .then(jobs => {
        const jobsList = document.getElementById('jobsList');
        jobsList.innerHTML = '';
        jobs.forEach(job => {
            const jobItem = document.createElement('li');
            jobItem.className = 'list-group-item';
            jobItem.textContent = job.description;
            jobsList.appendChild(jobItem);
        });
    });
}

function fetchQuestion() {
    fetch('/generate-interview-question', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({job_description: "Sample job description"}) // Use actual job description as needed
    })
    .then(response => response.json())
    .then(data => {
        const questionArea = document.getElementById('questionArea');
        questionArea.innerHTML = `<p>${data.question}</p>`;
        const emotionHolder = document.createElement('input');
        emotionHolder.type = 'hidden';
        emotionHolder.id = 'emotionHolder';
        emotionHolder.value = data.emotion;
        questionArea.appendChild(emotionHolder);
    })
    .catch(error => console.error('Error:', error));
}

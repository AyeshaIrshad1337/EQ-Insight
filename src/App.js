import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [jobDescription, setJobDescription] = useState('');
  const [question, setQuestion] = useState('');
  const [emotion, setEmotion] = useState('');
  const [answer, setAnswer] = useState('');
  const [score, setScore] = useState('');
  const [error, setError] = useState('');

  const generateQuestion = async () => {
    try {
      const response = await axios.post('/generate-interview-question', {
        job_description: jobDescription
      });
      const { emotion, question } = response.data;
      setQuestion(question);
      setEmotion(emotion);
      setError('');
    } catch (error) {
      setError('Error fetching question. Please try again.');
    }
  };

  const submitAnswer = async () => {
    try {
      const response = await axios.post('/submit-answer', {
        answer: answer,
        emotion: emotion
      });
      const { score } = response.data;
      setScore(score);
      setError('');
    } catch (error) {
      setError('Error submitting answer. Please try again.');
    }
  };

  return (
    <div>
      <div>
        <label htmlFor="jobDescription">Job Description:</label>
        <textarea
          id="jobDescription"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />
      </div>
      <button onClick={generateQuestion}>Generate Question</button>
      
      {question && (
        <div>
          <p>Question: {question}</p>
          <div>
            <label htmlFor="answer">Your Answer:</label>
            <textarea
              id="answer"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
            />
            <button onClick={submitAnswer}>Submit Answer</button>
          </div>
        </div>
      )}
      
      {score && (
        <p>Score: {score}</p>
      )}
      
      {error && (
        <p>Error: {error}</p>
      )}
    </div>
  );
};

export default App;

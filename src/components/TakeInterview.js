import React, { useState } from 'react';
import axios from 'axios';

const InterviewTest = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [score, setScore] = useState('');
  const [error, setError] = useState('');

  const generateQuestion = async () => {
    try {
      const response = await axios.post('/generate-interview-question', {
        job_description: localStorage.getItem('jobDescription') || ''
      });
      const { emotion, question } = response.data;
      setQuestion(question);
      setError('');
    } catch (error) {
      setError('Error fetching question. Please try again.');
    }
  };

  const submitAnswer = async () => {
    try {
      const response = await axios.post('/submit-answer', {
        answer: answer,
        emotion: ''
      });
      const { score } = response.data;
      setScore(score);
      setError('');
    } catch (error) {
      setError('Error submitting answer. Please try again.');
    }
  };

  return (
    <div className="container">
      <h1>Interview Test</h1>
      <div className="question-container">
        <h2>Interview Question</h2>
        <p>{question}</p>
        <textarea
          className="form-control"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          placeholder="Type your answer here..."
        />
        <button className="btn btn-primary" onClick={submitAnswer}>
          Submit Answer
        </button>
        {score && (
          <div className="score-container">
            <h2>Score</h2>
            <p>{score}</p>
          </div>
        )}
        {error && <p className="error-msg">{error}</p>}
      </div>
    </div>
  );
};

export default InterviewTest;

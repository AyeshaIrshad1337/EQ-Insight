import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './App.css'; 

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
    <div className="container">
      <h1>Interview Question Generator</h1>
      <div className="form-group">
        <label htmlFor="jobDescription">Enter Job Description:</label>
        <textarea
          id="jobDescription"
          className="form-control"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          placeholder="Describe the job you're interviewing for..."
        />
      </div>
      <button className="btn btn-primary" onClick={generateQuestion}>Generate Question</button>
      
      {question && (
        <div className="question-container">
          <h2>Interview Question</h2>
          <p>{question}</p>
          <div className="form-group">
            <label htmlFor="answer">Your Answer:</label>
            <textarea
              id="answer"
              className="form-control"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder="Type your answer here..."
            />
            <button className="btn btn-primary" onClick={submitAnswer}>Submit Answer</button>
          </div>
        </div>
      )}
      
      {score && (
        <div className="score-container">
          <h2>Score</h2>
          <p>{score}</p>
        </div>
      )}
      
      {error && (
        <div className="error-container">
          <p className="error-msg">{error}</p>
        </div>
      )}

      {/* Render job description as Markdown */}
      <div className="job-description">
        <h2>Job Description Preview</h2>
        <ReactMarkdown>{jobDescription}</ReactMarkdown>
      </div>
    </div>
  );
};

export default App;

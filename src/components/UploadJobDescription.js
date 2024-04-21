import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';


const JobDescriptionUpload = () => {
  const [jobDescription, setJobDescription] = useState('');
  const history = useHistory();

  const handleUpload = async () => {
    try {
      await axios.post('/upload-job-description', { jobDescription });
      history.push('/interview');
    } catch (error) {
      console.error('Error uploading job description:', error);
    }
  };
  
  return (
    <div className="container">
      <h1>Upload Job Description</h1>
      <textarea
        className="form-control"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        placeholder="Describe the job you're interviewing for..."
      />
      <button className="btn btn-primary" onClick={handleUpload}>
        Start Interview
      </button>
    </div>
  );
};

export default JobDescriptionUpload;

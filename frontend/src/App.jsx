import React, { useState } from 'react';
import axios from 'axios';
import Sidebar from './components/Sidebar';
import ResultArea from './components/ResultArea'; 
import './App.css';

function App() {
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post('/api/plan', data);
      setResult(response.data.itinerary);
    } catch (error) {
      console.error("Error generating trip:", error);
      setResult("### ❌ Error\nSomething went wrong. Please check if the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <Sidebar onGenerate={handleGenerate} loading={loading} />
      <main className="content">
        {loading ? (
          <div className="loading-state">
            <div className="spinner"></div>
            <p>Agents are researching your trip... This may take a minute.</p>
          </div>
        ) : (
          <div className="result-container">
            {result ? (
              <ResultArea itinerary={result} />
            ) : (
              <div className="welcome">
                <h1>Ready for your next adventure?</h1>
                <p>Fill out the form to start the AI planning process.</p>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
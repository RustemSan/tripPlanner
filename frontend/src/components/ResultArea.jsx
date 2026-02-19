import React from 'react';
import { ClipboardCheck } from 'lucide-react'; 
import ReactMarkdown from 'react-markdown';

const ResultArea = ({ itinerary }) => {
  if (!itinerary) return null;

  const copyToClipboard = () => {
    navigator.clipboard.writeText(itinerary);
    alert("Copied to clipboard!");
  };

  return (
    <div className="result-area">
      <div className="result-header">
        <h3>Generated Itinerary</h3>
        <div className="result-actions">
          <button onClick={copyToClipboard} title="Copy text">
            <ClipboardCheck size={18} />
          </button>
        </div>
      </div>
      <div className="itinerary-content">
        {}
        <ReactMarkdown>{itinerary}</ReactMarkdown>
      </div>
    </div>
  );
};

export default ResultArea;
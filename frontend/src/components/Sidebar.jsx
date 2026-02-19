import React, { useState } from 'react';
import { Plane, MapPin, Calendar, Heart, Loader2 } from 'lucide-react';

const Sidebar = ({ onGenerate, loading }) => {
  const [formData, setFormData] = useState({
    origin: '',
    cities: '',
    date_range: '',
    interests: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onGenerate(formData);
  };

  return (
    <div className="sidebar">
      <h2 className="title">🌍 Trip Planner AI</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label><MapPin size={16}/> From:</label>
          <input 
            type="text" 
            placeholder="Prague, CZ"
            value={formData.origin}
            onChange={(e) => setFormData({...formData, origin: e.target.value})}
            required
          />
        </div>

        <div className="input-group">
          <label><Plane size={16}/> Destinations:</label>
          <input 
            type="text" 
            placeholder="Barcelona, Paris..."
            value={formData.cities}
            onChange={(e) => setFormData({...formData, cities: e.target.value})}
            required
          />
        </div>

        <div className="input-group">
          <label><Calendar size={16}/> Dates:</label>
          <input 
            type="text" 
            placeholder="June, 7 days"
            value={formData.date_range}
            onChange={(e) => setFormData({...formData, date_range: e.target.value})}
            required
          />
        </div>

        <div className="input-group">
          <label><Heart size={16}/> Interests:</label>
          <textarea 
            placeholder="Football, Art, Running..."
            value={formData.interests}
            onChange={(e) => setFormData({...formData, interests: e.target.value})}
            required
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? <Loader2 className="animate-spin" /> : "Generate Itinerary"}
        </button>
      </form>
    </div>
  );
};

export default Sidebar;
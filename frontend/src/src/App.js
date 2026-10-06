import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";
import './App.css'; // Import the CSS file

const App = () => {
  const [activeTab, setActiveTab] = useState('main');
  const [startDate, setStartDate] = useState(new Date());

  const handleTabChange = (tabName) => {
    setActiveTab(tabName);
  };

  return (
    <div className="app-container">
      <header className="tabs">
        <button
          onClick={() => handleTabChange('main')}
          className={activeTab === 'main' ? 'active' : ''}
        >
          Main Tab
        </button>
        <button
          onClick={() => handleTabChange('settings')}
          className={activeTab === 'settings' ? 'active' : ''}
        >
          Settings Tab
        </button>
      </header>

      <main className="content">
        {activeTab === 'main' && (
          <div className="columns-container">
            {/* Left Column (30%) */}
            <div className="left-column">
              <h2>Date Selector</h2>
              <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
              <p>Selected Date: {startDate.toDateString()}</p>
            </div>

            {/* Right Column (70%) */}
            <div className="right-column">
              <h2>Main Content Area</h2>
              <p>This area takes up 70% of the space.</p>
              <p>Content related to the selected date can go here.</p>
            </div>
          </div>
        )}
        {activeTab === 'settings' && (
          <div>
            <h2>Settings Tab Content</h2>
            <p>This is where your application settings would go.</p>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;

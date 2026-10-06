import React, { useEffect, useState } from 'react';
import './App.css'; // Import the CSS file
import Home from './pages/Home';
import Settings from './pages/Settings';
import { hasSettings } from './api';

const App = () => {
  const [activeTab, setActiveTab] = useState(null);

  useEffect(() => {
    hasSettings().then((exists) => setActiveTab(exists ? 'main' : 'settings'));
  }, []);

  const handleTabChange = (tabName) => {
    setActiveTab(tabName);
  };

  if (activeTab === null) {
    return <p>Loading...</p>;
  }

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
        {activeTab === 'main' && <Home />}
        {activeTab === 'settings' && (
          <Settings onSaved={() => handleTabChange('main')} />
        )}
      </main>
    </div>
  );
};

export default App;

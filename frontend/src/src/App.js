import React, { useState } from 'react';
import './App.css'; // Import the CSS file
import Home from './pages/Home';
import Settings from './pages/Settings';

const App = () => {
  const [activeTab, setActiveTab] = useState('main');

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
        {activeTab === 'main' && <Home />}
        {activeTab === 'settings' && (
          <Settings onSaved={() => handleTabChange('main')} />
        )}
      </main>
    </div>
  );
};

export default App;

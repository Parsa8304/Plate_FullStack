// src/App.js
import React, { useState } from 'react';
import Register from './components/Register';
import Login from './components/Login';
import PlateDetect from './components/PlateDetect';

function App() {
  const [token, setToken] = useState('');
  const [showRegister, setShowRegister] = useState(false);

  const buttonStyle = (active) => ({
    padding: '10px 24px',
    margin: '0 5px',
    border: 'none',
    borderRadius: 6,
    fontSize: 16,
    cursor: 'pointer',
    background: active ? '#1976d2' : '#e3e3e3',
    color: active ? '#fff' : '#1976d2',
    fontWeight: active ? 'bold' : 'normal',
    boxShadow: active ? '0 2px 8px rgba(25,118,210,0.12)' : 'none',
    transition: 'all 0.2s'
  });

  if (token) {
    return <PlateDetect token={token} />;
  }

  return (
    <div>
      <div style={{textAlign: 'center', margin: 20}}>
        <button
          onClick={() => setShowRegister(false)}
          style={buttonStyle(!showRegister)}
        >
          Login
        </button>
        <button
          onClick={() => setShowRegister(true)}
          style={buttonStyle(showRegister)}
        >
          Register
        </button>
      </div>
      {showRegister ? <Register /> : <Login setToken={setToken} />}
    </div>
  );
}

export default App;

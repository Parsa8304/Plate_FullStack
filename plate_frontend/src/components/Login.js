// src/components/Login.js
import React, { useState } from 'react';
import axios from 'axios';

export default function Login({ setToken }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:8000/login', { username, password });
      setToken(res.data.token);
      setMsg('✅ Logged in!');
    } catch (err) {
      setMsg('❌ Error: ' + (err.response?.data?.error || 'Unknown error'));
    }
  };

  return (
    <div style={{
      maxWidth: 350,
      margin: '40px auto',
      padding: 24,
      borderRadius: 12,
      boxShadow: '0 2px 12px rgba(0,0,0,0.12)',
      background: '#fff'
    }}>
      <h2 style={{textAlign: 'center', color: '#1976d2'}}>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          style={{
            width: '100%',
            padding: '10px',
            margin: '10px 0',
            borderRadius: 6,
            border: '1px solid #ccc',
            fontSize: 16
          }}
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <input
          type="password"
          style={{
            width: '100%',
            padding: '10px',
            margin: '10px 0',
            borderRadius: 6,
            border: '1px solid #ccc',
            fontSize: 16
          }}
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <button
          type="submit"
          style={{
            width: '100%',
            padding: '10px',
            background: '#1976d2',
            color: '#fff',
            border: 'none',
            borderRadius: 6,
            fontSize: 16,
            cursor: 'pointer',
            marginTop: 10
          }}
        >
          Login
        </button>
        <div style={{marginTop: 16, textAlign: 'center', color: msg.startsWith('✅') ? 'green' : 'red'}}>
          {msg}
        </div>
      </form>
    </div>
  );
}
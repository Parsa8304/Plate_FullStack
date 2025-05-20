// src/components/PlateDetect.js
import React, { useState } from 'react';
import axios from 'axios';

export default function PlateDetect({ token }) {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    const formData = new FormData();
    formData.append('image', file);
    try {
      const res = await axios.post('http://127.0.0.1:8000/detect', formData, {
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'multipart/form-data'
        }
      });
      setResult('✅ Plate Number: ' + res.data.plate_number);
    } catch (err) {
        console.error(err);
      setResult('❌ Error: ' + (err.response?.data?.error || 'Unknown error'));
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
      <h2 style={{textAlign: 'center', color: '#1976d2'}}>Detect Plate</h2>
      <div style={{textAlign: 'center', marginBottom: 16}}>
        <a
          href="http://127.0.0.1:8000/detect/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <button
            style={{
              padding: '8px 18px',
              background: '#43a047',
              color: '#fff',
              border: 'none',
              borderRadius: 6,
              fontSize: 15,
              cursor: 'pointer',
              marginBottom: 10
            }}
            type="button"
          >
            Go to Plate Detection Endpoint
          </button>
        </a>
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="image/*"
          style={{
            width: '100%',
            padding: '10px',
            margin: '10px 0',
            borderRadius: 6,
            border: '1px solid #ccc',
            fontSize: 16
          }}
          onChange={e => setFile(e.target.files[0])}
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
          Upload & Detect
        </button>
        <div style={{marginTop: 16, textAlign: 'center', color: result.startsWith('✅') ? 'green' : 'red'}}>
          {result}
        </div>
      </form>
    </div>
  );
}
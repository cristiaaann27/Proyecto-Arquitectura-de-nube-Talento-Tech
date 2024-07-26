import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [response, setResponse] = useState('');

  const handleVoiceCommand = async () => {
    try {
      const res = await axios.post('http://localhost:5000/voice-command', {});
      setResponse(res.data.message);
    } catch (error) {
      console.error(error);
      setResponse('Error processing voice command');
    }
  };

  return (
    <div className="App">
      <h1>Voice Command Task Assistant</h1>
      <button onClick={handleVoiceCommand}>Send Command</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default App;

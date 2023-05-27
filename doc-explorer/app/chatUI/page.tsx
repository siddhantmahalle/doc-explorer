"use client"

import React, { useState, useEffect } from 'react';
import '@/app/css/chat-ui.css';

const ChatUI = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [currentMessage, setCurrentMessage] = useState('');

  const handleSendMessage = async () => {
    if (currentMessage.trim() !== '') {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: currentMessage }),
      });

      if (response.ok) {
        const data = await response.json();
        const botResponse = data.response;
        setMessages([...messages, currentMessage, botResponse]);
      } else {
        console.error('Error sending message');
      }

      setCurrentMessage('');
    }
  };

  const handleChangeMessage = (e: React.ChangeEvent<HTMLInputElement>) => {
    setCurrentMessage(e.target.value);
  };

  useEffect(() => {
  const chatMessages = document.getElementById('chat-messages');
  if (chatMessages) {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
  }, [messages]);


  return (
    <div className="center">
      <div className="title-container">
        <h1 className="title">Ask your Documents</h1>
      </div>
      <div className="chat-container">
        <div className="chat-messages" id="chat-messages">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`chat-message ${index % 2 === 0 ? 'user-message' : ''}`}
            >
              {message}
            </div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            placeholder="Type your question"
            value={currentMessage}
            onChange={handleChangeMessage}
            className="input-box"
          />
          <button className="send-icon" onClick={handleSendMessage}>
            <span className="send-icon-inner"></span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatUI;

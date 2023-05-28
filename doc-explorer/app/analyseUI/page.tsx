"use client"

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import '@/app/css/analyse-ui.css';

const AnalyseUI = () => {
  const router = useRouter();
  const [showButton, setShowButton] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowButton(true);
    }, 3000);

    return () => {
      clearTimeout(timer); // Clean up the timer on component unmount
    };
  }, []);

  const handleDoneClick = () => {
    router.push('/chatUI')
  };

  return (
    <div className="title-container">
      <h1 className={`title-body${showButton ? ' stop-animation' : ''}`}>
        Analysing your Data
      </h1>
      {showButton && (
        <button className="done-button" onClick={handleDoneClick}>
          Ask Questions
        </button>
      )}
    </div>
  );
};

export default AnalyseUI;

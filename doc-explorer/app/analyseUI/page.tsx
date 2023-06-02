"use client"

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import '@/app/css/analyse-ui.css';

const AnalyseUI = () => {
  const router = useRouter();
  const [showButton, setShowButton] = useState(false);

  useEffect(() => {
    const fetchProcessingStatus = async () => {

      const response = await fetch('/api/process_status',
          {
          method: 'POST',
        });
      const data = await response.json();

      if (data.status == 'complete') {
        setShowButton(true);
      }
    };

    fetchProcessingStatus()

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

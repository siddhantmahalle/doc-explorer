"use client";

import { useRouter } from 'next/navigation';
import '@/app/css/dashboard.css';

const Dashboard = () => {
  const router = useRouter();

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    router.push('/uploadUI');
  };

  return (
    <div className="title-container">
      <h1 className="title-body">Doc Explorer App</h1>
      <div className="subtitle-container">
        <h2 className="subtitle-body">Upload your documents and ask questions</h2>
      </div>
      <div className="submit-container">
        <form onSubmit={onSubmit}>
          <button type="submit" className="submit-button">
            <h2>Analyse your documents</h2>
          </button>
        </form>
      </div>
    </div>
  );
};

export default Dashboard;

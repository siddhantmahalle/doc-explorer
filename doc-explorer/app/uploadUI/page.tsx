"use client";
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import '@/app/css/upload-ui.css';

interface UploadUIProps {
  onUploadComplete: () => void;
}

const UploadUI = ({ onUploadComplete }: UploadUIProps) => {
  const [file, setFile] = useState<File | null>(null);
  const router = useRouter();

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      setFile(files[0]);
    }
  };

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (file) {
      const formData = new FormData();
      formData.append('file', file);
      try {
        const response = await fetch('/api/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          console.log('File uploaded successfully');
          // Handle successful upload
        } else {
          console.error('File upload failed');
          // Handle upload failure
        }

        router.push('/analyseUI');
      } catch (error) {
        console.error('Error occurred during file upload', error);
        // Handle upload error
      }
    }
  };

  return (
    <div className="center">
      <div className="upload-container">
        <div className="message">Choose the files to explore</div>
        <form onSubmit={onSubmit} className="upload-form">
          <input type="file" id="file-upload" onChange={onChange} className="custom-file-upload" />
          <button type="submit" className="upload-button">
            Upload
          </button>
        </form>
      </div>
    </div>
  );
};

export default UploadUI;

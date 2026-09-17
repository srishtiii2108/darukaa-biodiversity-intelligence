import { useState } from 'react';
import AppShell from './components/Layout/AppShell';
import ContextPanel from './components/Context/ContextPanel';
import ChatWorkspace from './components/Chat/ChatWorkspace';
import UploadModal from './components/Upload/UploadModal';
import { getSessionId, generateNewSession } from './utils/session';

export default function App() {
  const [sessionId, setSessionId] = useState(getSessionId());
  const [isUploadModalOpen, setIsUploadModalOpen] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  
  const [contextData, setContextData] = useState({
    soil_health: { ph: null, organic_carbon_percent: null, moisture_level: null },
    climate: { temperature_celsius: null, rainfall_pattern: null },
    land_use: null,
    region: null
  });

  const handleNewAssessment = () => {
    const newId = generateNewSession();
    setSessionId(newId);
    setUploadedFiles([]);
    setContextData({
      soil_health: { ph: null, organic_carbon_percent: null, moisture_level: null },
      climate: { temperature_celsius: null, rainfall_pattern: null },
      land_use: null,
      region: null
    });
  };

  const handleUploadSuccess = (fileName) => {
    setUploadedFiles((prev) => [...prev, fileName]);
  };

  return (
    <>
      <AppShell 
        sidebar={<ContextPanel contextData={contextData} uploadedFiles={uploadedFiles} />}
        onNewAssessment={handleNewAssessment}
      >
        <ChatWorkspace 
          key={sessionId} 
          sessionId={sessionId}
          onContextUpdate={setContextData} 
          onOpenUpload={() => setIsUploadModalOpen(true)}
        />
      </AppShell>

      <UploadModal 
        isOpen={isUploadModalOpen} 
        onClose={() => setIsUploadModalOpen(false)}
        sessionId={sessionId}
        onUploadSuccess={handleUploadSuccess}
      />
    </>
  );
}
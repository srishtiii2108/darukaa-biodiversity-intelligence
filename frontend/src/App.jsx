import { useState } from 'react';
import AppShell from './components/Layout/AppShell';
import ContextPanel from './components/Context/ContextPanel';
import ChatWorkspace from './components/Chat/ChatWorkspace';

export default function App() {
  const [contextData, setContextData] = useState({
    soil_health: { ph: null, organic_carbon_percent: null, moisture_level: null },
    climate: { temperature_celsius: null, rainfall_pattern: null },
    land_use: null,
    region: null
  });

  return (
    <AppShell sidebar={<ContextPanel contextData={contextData} />}>
      <ChatWorkspace onContextUpdate={setContextData} />
    </AppShell>
  );
}
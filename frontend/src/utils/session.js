export const getSessionId = () => {
  let sessionId = sessionStorage.getItem('darukaa_session_id');
  if (!sessionId) {
    sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now();
    sessionStorage.setItem('darukaa_session_id', sessionId);
  }
  return sessionId;
};

export const generateNewSession = () => {
  const sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now();
  sessionStorage.setItem('darukaa_session_id', sessionId);
  return sessionId;
};
export const getSessionId = () => {
  let sessionId = sessionStorage.getItem('darukaa_session_id');
  if (!sessionId) {
    // Generate a simple unique session ID
    sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now();
    sessionStorage.setItem('darukaa_session_id', sessionId);
  }
  return sessionId;
};

export const resetSession = () => {
  sessionStorage.removeItem('darukaa_session_id');
};
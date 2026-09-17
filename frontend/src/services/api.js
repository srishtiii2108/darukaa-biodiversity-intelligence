const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

export const sendChatMessage = async (sessionId, userMessage) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_id: sessionId,
        user_message: userMessage,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to connect to Darukaa Intelligence.');
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const uploadScientificDocument = async (file, sessionId) => {
  console.log("[API] uploadScientificDocument called");
  console.log("[API] API base URL:", API_BASE_URL);
  
  const endpoint = `${API_BASE_URL}/api/upload`;
  console.log("[API] Endpoint:", endpoint);

  const formData = new FormData();
  console.log("[API] FormData created");
  
  formData.append('file', file);
  console.log("[API] File appended:", file.name);
  
  formData.append('session_id', sessionId || 'default_session');
  console.log("[API] Session ID appended:", sessionId);

  try {
    console.log("[API] About to send request via fetch");
    const response = await fetch(endpoint, {
      method: 'POST',
      body: formData,
      // NOTE: DO NOT manually set Content-Type header when using FormData! 
      // The browser automatically assigns multipart/form-data and the correct boundary.
    });

    console.log("[API] Response received. Status:", response.status);
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error("[API] Server error response body:", errorText);
      throw new Error(`Upload failed (${response.status}): ${errorText || response.statusText}`);
    }

    const data = await response.json();
    console.log("[API] Response body JSON:", data);
    return data;
  } catch (error) {
    console.error('[API] Upload execution exception:', error);
    throw error;
  }
};
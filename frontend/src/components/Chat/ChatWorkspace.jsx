import { useState, useRef, useEffect } from 'react';
import HeroState from './HeroState';
import ChatInput from './ChatInput';
import MessageBubble from './MessageBubble';
import RecommendationCard from '../Recommendation/RecommendationCard';
import { sendChatMessage } from '../../services/api';

export default function ChatWorkspace({ sessionId, onContextUpdate, onOpenUpload }) {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };
  useEffect(() => { scrollToBottom(); }, [messages, isLoading]);

  const handleSelectPrompt = (text) => {
    setInput(text.replace(/['"]/g, '')); 
  };

  const handleSendMessage = async (userMessage) => {
    const newMsg = { role: 'user', content: userMessage };
    setMessages((prev) => [...prev, newMsg]);
    setIsLoading(true);
    setInput('');

    try {
      const data = await sendChatMessage(sessionId, userMessage);

      if (data && data.updated_context) {
        onContextUpdate(data.updated_context);
      }

      setMessages((prev) => [
        ...prev,
        { 
          role: 'ai', 
          content: data?.reply || "No valid response received from the intelligence engine.", 
          isRecommendation: !!data?.is_recommendation 
        }
      ]);
    } catch (error) {
      console.error("Chat Error:", error);
      setMessages((prev) => [
        ...prev,
        { role: 'ai', content: 'Unable to reach the environmental intelligence service. Please try again.', isRecommendation: false }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex-1 flex flex-col h-full relative">
      <div className="flex-1 overflow-y-auto custom-scrollbar flex flex-col pt-10">
        
        {messages.length === 0 ? (
          <HeroState onSelectPrompt={handleSelectPrompt} />
        ) : (
          <div className="w-full pb-4">
            {messages.map((msg, idx) => (
              msg.isRecommendation ? (
                <RecommendationCard key={`rec-${idx}`} message={msg} />
              ) : (
                <MessageBubble key={`msg-${idx}`} message={msg} />
              )
            ))}
            
            {isLoading && (
              <div className="flex w-full justify-start mb-6 px-6">
                <div className="flex gap-4 max-w-[850px] w-full mx-auto">
                  <div className="w-8 h-8 rounded-full bg-darukaa-green text-white flex items-center justify-center shrink-0 mt-1">
                    <span className="animate-pulse">...</span>
                  </div>
                  <div className="px-5 py-4 bg-white border border-darukaa-border rounded-2xl shadow-sm">
                    <p className="text-[14px] text-darukaa-muted animate-pulse">Analyzing environmental context...</p>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>

      <div className="shrink-0 bg-gradient-to-t from-[#FAFCFB] via-[#FAFCFB] to-transparent pt-6">
        <ChatInput 
          input={input} 
          setInput={setInput} 
          onSendMessage={handleSendMessage} 
          disabled={isLoading} 
          onOpenUpload={onOpenUpload}
        />
      </div>
    </div>
  );
}
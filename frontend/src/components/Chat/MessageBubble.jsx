import { Leaf } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

export default function MessageBubble({ message }) {
  const isAI = message.role === 'ai';

  return (
    <div className={`flex w-full ${isAI ? 'justify-start' : 'justify-start'} mb-6 px-6`}>
      <div className="flex gap-4 max-w-[850px] w-full mx-auto">
        
        {/* Avatar */}
        <div className="shrink-0 mt-1">
          {isAI ? (
            <div className="w-8 h-8 rounded-full bg-darukaa-green text-white flex items-center justify-center shadow-sm">
              <Leaf className="w-4 h-4" />
            </div>
          ) : (
            <div className="w-8 h-8 rounded-full bg-[#E8F0EA] text-darukaa-green flex items-center justify-center text-[11px] font-bold border border-darukaa-green/10">
              AS
            </div>
          )}
        </div>

        {/* Message Content */}
        <div className={`flex-1 px-5 py-4 rounded-2xl ${
          isAI 
            ? 'bg-white border border-darukaa-border shadow-sm' 
            : 'bg-[#F4F9F5] border border-[#E8F0EA] text-darukaa-text'
        }`}>
          {isAI ? (
            <div className="prose prose-sm max-w-none prose-p:leading-relaxed prose-headings:font-serif prose-headings:text-darukaa-text prose-a:text-darukaa-green prose-strong:text-darukaa-text">
              <ReactMarkdown>{message.content}</ReactMarkdown>
            </div>
          ) : (
            <p className="text-[14px] leading-relaxed">{message.content}</p>
          )}
        </div>
        
      </div>
    </div>
  );
}
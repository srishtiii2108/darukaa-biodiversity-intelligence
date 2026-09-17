import { Paperclip, ArrowUp } from 'lucide-react';

export default function ChatInput({ input, setInput, onSendMessage, disabled }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() && !disabled) {
      onSendMessage(input.trim());
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="w-full max-w-[850px] mx-auto px-6 pb-6 pt-2">
      <form
        onSubmit={handleSubmit}
        className="relative flex items-center w-full bg-white border border-darukaa-border rounded-full shadow-sm px-2 py-2 focus-within:border-darukaa-green/30 focus-within:shadow-subtle transition-all"
      >
        <button type="button" className="p-3 text-darukaa-muted hover:text-darukaa-text transition-colors shrink-0">
          <Paperclip className="w-4 h-4" />
        </button>
        
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask about your land, ecosystem or biodiversity concern..."
          className="flex-1 bg-transparent border-none outline-none text-[14px] text-darukaa-text px-2 placeholder:text-darukaa-muted"
          disabled={disabled}
        />
        
        <button
          type="submit"
          disabled={!input.trim() || disabled}
          className="w-10 h-10 rounded-full bg-darukaa-green text-white flex items-center justify-center shrink-0 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-opacity-90 transition-all"
        >
          <ArrowUp className="w-5 h-5" />
        </button>
      </form>
      <div className="text-center mt-3">
        <span className="text-[10px] text-darukaa-muted font-medium">
          AI-generated environmental guidance • Grounded in scientific evidence
        </span>
      </div>
    </div>
  );
}
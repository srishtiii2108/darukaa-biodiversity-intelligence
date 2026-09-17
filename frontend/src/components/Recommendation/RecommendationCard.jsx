import { Leaf, CheckCircle2 } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

export default function RecommendationCard({ message }) {
  // 🛡️ Safety Check: Agar kisi wajah se message undefined aata hai toh app crash nahi hoga
  if (!message || typeof message.content === 'undefined') return null;

  return (
    <div className="flex w-full justify-start mb-8 px-6">
      <div className="flex gap-4 max-w-[850px] w-full mx-auto">
        
        {/* Left Icon (Darukaa AI) */}
        <div className="shrink-0 mt-1">
          <div className="w-8 h-8 rounded-full bg-darukaa-green text-white flex items-center justify-center shadow-sm">
            <Leaf className="w-4 h-4" />
          </div>
        </div>

        {/* Premium Recommendation Card */}
        <div className="flex-1 bg-white border border-darukaa-green/30 rounded-2xl shadow-sm overflow-hidden flex flex-col">
          
          {/* Card Header */}
          <div className="flex items-center justify-between px-6 py-4 border-b border-darukaa-border bg-[#FAFCFB]">
            <div className="flex items-center gap-2">
              <Leaf className="w-4 h-4 text-darukaa-green" />
              <span className="text-[11px] font-bold tracking-[0.15em] text-darukaa-text uppercase">Recommendation</span>
            </div>
            <div className="flex items-center gap-1.5 bg-[#E8F0EA] text-darukaa-green px-2.5 py-1 rounded-full border border-darukaa-green/20">
              <CheckCircle2 className="w-3 h-3" />
              <span className="text-[10px] font-bold uppercase tracking-wide">Evidence-based</span>
            </div>
          </div>

          {/* Card Body (Markdown styled to look premium) */}
          <div className="p-6 prose prose-sm max-w-none 
            prose-p:leading-relaxed prose-p:text-[14px] prose-p:text-darukaa-text
            prose-strong:text-darukaa-green prose-strong:font-semibold
            prose-ul:list-none prose-ul:pl-0 prose-li:relative prose-li:pl-5
            prose-li:before:content-['•'] prose-li:before:absolute prose-li:before:left-0 prose-li:before:text-darukaa-green prose-li:before:font-bold
            prose-a:text-darukaa-green prose-a:no-underline hover:prose-a:underline
            [&>p:first-child]:font-serif [&>p:first-child]:text-2xl [&>p:first-child]:text-darukaa-text [&>p:first-child]:mb-6 [&>p:first-child>strong]:text-darukaa-text [&>p:first-child>strong]:font-medium
          ">
            <ReactMarkdown>{message.content || ""}</ReactMarkdown>
          </div>

          {/* Subtle Footer */}
          <div className="bg-[#F4F9F5] px-6 py-3 border-t border-[#E8F0EA]">
            <p className="text-[12px] text-darukaa-green flex items-center gap-2">
              <Leaf className="w-3 h-3" />
              This approach aligns with multi-metric environmental intelligence parameters.
            </p>
          </div>
          
        </div>
      </div>
    </div>
  );
}
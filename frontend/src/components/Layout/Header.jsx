import { Leaf, Plus } from 'lucide-react';

export default function Header() {
  return (
    <header className="h-[72px] bg-white border-b border-darukaa-border flex items-center justify-between px-6 shrink-0 z-10">
      {/* Left: Brand Logo & Taglines */}
      <div className="flex items-center gap-3">
        {/* Placeholder for actual logo, using Lucide Leaf for now */}
        <Leaf className="w-8 h-8 text-darukaa-green" />
        <div className="flex flex-col">
          <span className="font-serif text-[22px] font-bold text-darukaa-green leading-none">Darukaa.Earth</span>
          <span className="text-[9px] tracking-[0.2em] text-darukaa-muted font-semibold mt-1 uppercase">Biodiversity Intelligence</span>
        </div>
        <div className="hidden md:block ml-6 pl-6 border-l border-darukaa-border text-[11px] text-darukaa-muted leading-[1.3]">
          Healthier<br/>Ecosystems<br/>Brighter Tomorrows
        </div>
      </div>

      {/* Right: Status & Actions */}
      <div className="flex items-center gap-5">
        <div className="hidden md:flex items-center gap-2 text-[13px] font-medium text-darukaa-text">
          <span className="w-2 h-2 bg-emerald-500 rounded-full"></span>
          Environmental AI Online
        </div>
        <button className="bg-darukaa-green text-white px-4 py-2 rounded-full text-sm font-medium flex items-center gap-2 hover:bg-opacity-90 transition-all shadow-sm">
          <Plus className="w-4 h-4" />
          New Assessment
        </button>
        <div className="w-9 h-9 rounded-full bg-[#E8F0EA] text-darukaa-green flex items-center justify-center text-sm font-bold border border-darukaa-green/10">
          SA
        </div>
      </div>
    </header>
  );
}
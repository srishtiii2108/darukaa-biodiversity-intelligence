import { Sprout, Cloud, TreePine, ArrowRight } from 'lucide-react';

function PromptCard({ icon: Icon, label, text, onClick }) {
  return (
    <button
      onClick={() => onClick(text)}
      className="flex items-start gap-4 p-5 bg-white border border-darukaa-border rounded-2xl hover:border-darukaa-green/30 hover:shadow-subtle transition-all text-left group"
    >
      <div className="bg-[#E8F0EA] p-2 rounded-lg text-darukaa-green shrink-0">
        <Icon className="w-5 h-5" />
      </div>
      <div className="flex-1">
        <h4 className="text-[10px] font-bold tracking-widest text-darukaa-text uppercase mb-2">{label}</h4>
        <p className="text-[13px] text-darukaa-muted leading-relaxed">"{text}"</p>
      </div>
      <div className="w-6 h-6 rounded-full bg-[#FAFCFB] border border-darukaa-border flex items-center justify-center text-darukaa-muted group-hover:bg-darukaa-green group-hover:text-white transition-colors shrink-0 mt-1">
        <ArrowRight className="w-3 h-3" />
      </div>
    </button>
  );
}

export default function HeroState({ onSelectPrompt }) {
  return (
    <div className="flex flex-col items-center justify-center w-full max-w-[850px] mx-auto mt-12 px-6">
      <span className="text-[10px] font-bold tracking-[0.2em] text-darukaa-muted uppercase mb-4">
        AI Environmental Scientist
      </span>
      <h1 className="font-serif text-4xl md:text-5xl font-medium text-darukaa-text text-center leading-[1.15] mb-4">
        Understand your environment.<br />Act on what matters.
      </h1>
      <p className="text-[14px] text-darukaa-muted text-center max-w-xl mb-12">
        Connect soil, climate, land-use and biodiversity signals to evidence-backed recommendations.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 w-full">
        <PromptCard
          icon={Sprout}
          label="Low Soil Carbon"
          text="My soil organic carbon is 0.3% and rainfall is low."
          onClick={onSelectPrompt}
        />
        <PromptCard
          icon={Cloud}
          label="Climate Stress"
          text="Rainfall has become increasingly irregular on my land."
          onClick={onSelectPrompt}
        />
        <PromptCard
          icon={TreePine}
          label="Biodiversity Loss"
          text="Biodiversity is declining in my agricultural area."
          onClick={onSelectPrompt}
        />
      </div>
    </div>
  );
}
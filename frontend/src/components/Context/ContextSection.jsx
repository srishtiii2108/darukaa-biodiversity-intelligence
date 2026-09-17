export default function ContextSection({ icon: Icon, title, data }) {
  return (
    <div className="mb-5">
      <div className="flex items-center gap-2 mb-2 px-1">
        <div className="bg-[#E8F0EA] p-1.5 rounded-md text-darukaa-green">
          <Icon className="w-4 h-4" />
        </div>
        <h3 className="text-[11px] font-bold text-darukaa-text tracking-wider uppercase">{title}</h3>
      </div>
      <div className="space-y-1.5">
        {data.map((item, idx) => (
          <div key={idx} className="flex items-center justify-between py-1.5 px-3 border border-darukaa-border rounded-lg bg-white shadow-[0_1px_2px_rgba(0,0,0,0.02)]">
            <span className="text-[12px] text-darukaa-text">{item.label}</span>
            <span className={`text-[12px] ${item.value ? (item.highlight ? 'text-darukaa-green font-bold bg-[#E8F0EA] px-2 py-0.5 rounded' : 'text-darukaa-text font-medium') : 'text-darukaa-muted'}`}>
              {item.value || 'Not provided'}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
import Header from './Header';

export default function AppShell({ sidebar, children, onNewAssessment }) {
  return (
    <div className="h-screen w-full flex flex-col bg-[#FAFCFB] overflow-hidden">
      <Header onNewAssessment={onNewAssessment} />
      <div className="flex flex-1 overflow-hidden">
        <aside className="w-[320px] bg-[#FAFCFB] border-r border-darukaa-border flex-shrink-0 flex flex-col overflow-y-auto custom-scrollbar">
          {sidebar}
        </aside>
        <main className="flex-1 relative flex flex-col overflow-hidden bg-white/50">
          {children}
        </main>
      </div>
    </div>
  );
}
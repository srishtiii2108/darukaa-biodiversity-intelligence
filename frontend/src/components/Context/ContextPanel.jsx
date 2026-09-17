import { Sprout, Cloud, MapPin, Leaf } from 'lucide-react';
import ContextSection from './ContextSection';

export default function ContextPanel({ contextData }) {
  // Safely extract data with fallbacks for UI
  const soil = contextData?.soil_health || {};
  const climate = contextData?.climate || {};

  // Calculate detected variables for the status circle
  const allValues = [
    soil.ph, soil.organic_carbon_percent, soil.moisture_level,
    climate.rainfall_pattern, climate.temperature_celsius,
    contextData?.land_use, contextData?.region
  ];
  const detectedCount = allValues.filter(val => val !== null && val !== undefined && val !== '').length;

  return (
    <div className="p-5 flex flex-col min-h-full">
      <div className="flex-1">
        <h2 className="text-[11px] font-bold tracking-widest text-darukaa-text uppercase mb-1">Environmental Context</h2>
        <p className="text-[12px] text-darukaa-muted mb-6">What the AI currently understands</p>

        <ContextSection 
          icon={Sprout} title="Soil Health" 
          data={[
            { label: 'pH', value: soil.ph },
            { label: 'Organic Carbon', value: soil.organic_carbon_percent ? `${soil.organic_carbon_percent}%` : null, highlight: true },
            { label: 'Moisture', value: soil.moisture_level }
          ]} 
        />

        <ContextSection 
          icon={Cloud} title="Climate" 
          data={[
            { label: 'Rainfall', value: climate.rainfall_pattern, highlight: climate.rainfall_pattern === 'low' },
            { label: 'Temperature', value: climate.temperature_celsius ? `${climate.temperature_celsius}°C` : null }
          ]} 
        />

        <ContextSection 
          icon={Leaf} title="Land Use" 
          data={[{ label: 'Current', value: contextData?.land_use }]} 
        />

        <ContextSection 
          icon={MapPin} title="Region" 
          data={[{ label: 'Location', value: contextData?.region }]} 
        />
      </div>

      {/* Context Status & Brand Card */}
      <div className="mt-4 pt-6 border-t border-darukaa-border shrink-0">
        <h3 className="text-[11px] font-bold tracking-widest text-darukaa-text uppercase mb-4">Context Status</h3>
        
        <div className="flex items-center gap-3">
          {/* Simple CSS Circular Progress representation */}
          <div className="relative w-8 h-8 rounded-full border-[3px] border-darukaa-border flex items-center justify-center">
             {detectedCount > 0 && (
               <div className="absolute top-0 left-0 w-full h-full rounded-full border-[3px] border-darukaa-green border-r-transparent border-t-transparent transform -rotate-45"></div>
             )}
          </div>
          <span className="text-[12px] font-medium text-darukaa-text">
            {detectedCount} environmental variable{detectedCount !== 1 ? 's' : ''} detected
          </span>
        </div>

        {/* Premium Quote Card */}
        <div className="mt-6 p-4 bg-white border border-darukaa-border rounded-xl shadow-subtle relative overflow-hidden">
           <Leaf className="absolute -right-3 -bottom-3 w-16 h-16 text-[#F4F9F5] opacity-60" strokeWidth={1} />
           <p className="text-[13px] italic text-darukaa-text font-serif leading-relaxed mb-3 relative z-10">
             "Better data<br/>brings us closer<br/>to a healthier planet."
           </p>
           <span className="text-[11px] font-bold text-darukaa-green relative z-10">Darukaa.Earth</span>
        </div>
      </div>
    </div>
  );
}
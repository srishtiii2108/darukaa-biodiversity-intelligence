import os

def create_raw_texts():
    raw_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(raw_dir, exist_ok=True)

    fao_text = """Soil organic carbon (SOC) is a critical component of soil health. In semi-arid regions characterized by low rainfall, conventional monoculture practices rapidly deplete SOC. Integrating agroforestry and legume-based cover crops can reverse this trend. Studies show that agroforestry increases SOC by 15-25% over a 3-5 year period. The deep root systems of trees break hardpan soil structures, significantly enhancing soil moisture retention. This combined effect of higher SOC and moisture provides a resilient microhabitat that supports microbial diversity and prevents severe soil erosion, establishing a direct link between soil carbon management and biodiversity conservation."""
    
    ipcc_text = """Climate change exacerbates land degradation, particularly through altered rainfall patterns and prolonged drought. Reduced water availability directly threatens species richness and ecosystem resilience. Implementing landscape-level interventions, such as contour trenches and micro-catchments, reduces surface water runoff and increases local soil moisture by up to 40%. This water retention is crucial for the survival of drought-resistant native plant species. By maintaining these native vegetation patches, habitat fragmentation is reduced, allowing pollinator populations to stabilize even under warming temperatures."""
    
    unep_text = """Human impacts, including deforestation and chemical pollution, severely degrade ecosystem services. In agricultural zones, heavy reliance on synthetic pesticides alters soil pH and diminishes soil microbial diversity. Shifting towards organic Integrated Pest Management (IPM) and applying biochar can neutralize soil pH. This transition provides porous carbon structures for microbial recolonization. Ecosystem recovery is observable within 2-3 years, showcasing enhanced habitat diversity. Furthermore, replacing monoculture with mixed-cropping systems stabilizes the ecological niches needed for both insect and avian biodiversity."""

    with open(os.path.join(raw_dir, 'fao_soils_2021.txt'), 'w', encoding='utf-8') as f:
        f.write(fao_text)
    with open(os.path.join(raw_dir, 'ipcc_climate_land_2019.txt'), 'w', encoding='utf-8') as f:
        f.write(ipcc_text)
    with open(os.path.join(raw_dir, 'unep_peace_nature_2021.txt'), 'w', encoding='utf-8') as f:
        f.write(unep_text)
        
    print("✅ Raw scientific corpus built successfully in data/raw/")

if __name__ == "__main__":
    create_raw_texts()
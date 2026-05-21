# Planetary Ecological Integrity Index (PEII) — Methodology v0.1

## Why PEII Exists

PEII is the **single terminal metric** that Gaia Core optimizes for. Everything else is subordinate.

## Core Formula (v0.1)

```python
PEII = (0.35 × Biodiversity) 
     + (0.25 × Climate_Stability) 
     + (0.20 × Ocean_Freshwater_Health) 
     + (0.15 × Soil_Vitality) 
     + (0.05 × Atmospheric_Balance)
     - Tipping_Point_Penalties

Component Breakdown

Component,Weight,What It Measures,Ideal Direction
Biodiversity Health,0.35,"Species richness, evenness, habitat health",↑
Climate Stability,0.25,"Temperature, CO₂, CH₄, feedback loops",↑
Ocean & Freshwater,0.20,"pH, oxygen, coral/seagrass cover, pollution",↑
Soil Vitality,0.15,"Organic carbon, microbial activity, erosion",↑
Atmospheric Balance,0.05,"Aerosol loading, ozone, trace gases",↑

Core Rules

Long-term (50–500 years) perspective
Strong penalties for approaching tipping points
Human benefit is allowed only if it does not decrease long-term PEII
No trade-offs that sacrifice ecological integrity for short-term gains

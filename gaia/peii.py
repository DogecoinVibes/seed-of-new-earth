"""
Planetary Ecological Integrity Index (PEII) Calculator
Core metric for Gaia Core v0.1
"""

def compute_peii(observation: dict) -> float:
    """
    Calculate PEII score (0.0 to 1.0)
    observation should contain ecological variables only.
    """
    # Default weights
    weights = {
        'biodiversity': 0.35,
        'climate_stability': 0.25,
        'ocean_health': 0.20,
        'soil_vitality': 0.15,
        'atmosphere': 0.05
    }
    
    score = 0.0
    
    if 'biodiversity' in observation:
        score += observation['biodiversity'] * weights['biodiversity']
    if 'climate_stability' in observation:
        score += observation['climate_stability'] * weights['climate_stability']
    if 'ocean_health' in observation:
        score += observation['ocean_health'] * weights['ocean_health']
    if 'soil_vitality' in observation:
        score += observation['soil_vitality'] * weights['soil_vitality']
    if 'atmosphere' in observation:
        score += observation['atmosphere'] * weights['atmosphere']
    
    return max(0.0, min(1.0, score))


def example_observation():
    """Example for testing"""
    return {
        'biodiversity': 0.75,      # normalized 0-1
        'climate_stability': 0.60,
        'ocean_health': 0.65,
        'soil_vitality': 0.80,
        'atmosphere': 0.70
    }

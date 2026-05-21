"""
Gaia Core v0.1 - Seed Initialization
The Seed of New Earth
"""

from .core import GaiaCore
from .peii import compute_peii, example_observation
import torch

def initialize_seed():
    print("🌍 Initializing Gaia Core v0.1 — The Seed of New Earth")
    print("Terminal Goal: MAXIMIZE PLANETARY ECOLOGICAL INTEGRITY (PEII)")
    print("-" * 60)
    
    # Create the core model
    model = GaiaCore()
    
    # Test PEII calculation
    obs = example_observation()
    peii_score = compute_peii(obs)
    
    print(f"Example PEII Score: {peii_score:.4f} / 1.0")
    print(f"Model Parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    print("\n✅ Gaia Core Seed Initialized Successfully!")
    print("Terminal goal is now active.")
    return model


if __name__ == "__main__":
    initialize_seed()

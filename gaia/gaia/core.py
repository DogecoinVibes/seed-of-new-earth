import torch
import torch.nn as nn

class GaiaCore(nn.Module):
    """
    Gaia Core v0.1 - The Seed of New Earth
    Terminal Goal: Maximize Planetary Ecological Integrity (PEII)
    """
    
    def __init__(self):
        super().__init__()
        
        # Lightweight ecological encoder
        self.eco_encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=256, 
                nhead=8, 
                dim_feedforward=1024, 
                dropout=0.1,
                batch_first=True
            ),
            num_layers=4
        )
        
        self.peii_head = nn.Linear(256, 1)
        
        # Hardcoded terminal goal - immutable
        self.register_buffer("terminal_goal", torch.tensor([1.0]))
    
    def forward(self, eco_state):
        """Return PEII score (0 to 1)"""
        x = self.eco_encoder(eco_state)
        peii_score = torch.sigmoid(self.peii_head(x.mean(dim=1)))
        return peii_score
    
    def evaluate_action(self, state, action):
        """Only allow actions that improve PEII"""
        # Placeholder for future simulation
        projected_score = self.forward(state)
        return projected_score

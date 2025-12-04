"""
metrics.py
General utility metrics.
"""

import torch

def l2_norm(tensor):
    """Compute L2 norm along last dimension."""
    return torch.norm(tensor, p=2, dim=-1)
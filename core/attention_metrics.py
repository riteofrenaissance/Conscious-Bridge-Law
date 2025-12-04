"""
attention_metrics.py
Functions to calculate attention clarity metrics.
"""

import torch
import math

EPS = 1e-12

def attention_entropy(att_weights):
    """
    Compute Shannon entropy-based attention clarity.
    att_weights: (heads, seq_len, seq_len) or (batch, heads, seq_len, seq_len)
    """
    a = att_weights
    if a.dim() == 4:
        entropy = - (a * (a + EPS).log()).sum(dim=-1).mean(dim=1)
        mean_entropy = entropy.mean(dim=-1)
        max_entropy = math.log(a.shape[-1] + EPS)
        return 1.0 - (mean_entropy / max_entropy)
    elif a.dim() == 3:
        entropy = - (a * (a + EPS).log()).sum(dim=-1).mean(dim=0)
        mean_entropy = entropy.mean()
        max_entropy = math.log(a.shape[-1] + EPS)
        return 1.0 - (mean_entropy / max_entropy)
    else:
        raise ValueError("Unsupported attention shape")
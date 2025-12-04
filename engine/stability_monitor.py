"""
stability_monitor.py
Monitors model stability while traversing the bridge.
"""

def check_stability(h_t, prev_h_t, threshold=0.1):
    """
    Returns True if change is below threshold.
    """
    delta = torch.norm(h_t - prev_h_t, p=2)
    return delta.item() < threshold
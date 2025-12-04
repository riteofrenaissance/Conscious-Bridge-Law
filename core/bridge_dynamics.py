"""
bridge_dynamics.py
Handles transition dynamics on the conscious bridge.
"""

def smooth_transition(current, target, alpha=0.1):
    """
    Smoothly move from current to target using exponential smoothing.
    """
    return current + alpha * (target - current)

def adaptive_step_size(phi, base_step=0.05):
    """
    Adjust step size according to φ awareness value.
    """
    return base_step * (0.5 + phi)
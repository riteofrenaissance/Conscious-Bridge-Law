"""
temperature_adapter.py
Adjusts generation temperature based on φ awareness.
"""

def adapt_temperature(base_temp, phi, min_temp=0.5, max_temp=1.0):
    """
    Adjust temperature: higher φ → lower temperature (more deterministic).
    """
    return max(min_temp, min(max_temp, max_temp - phi * (max_temp - min_temp)))
"""
bridge_map.py
Defines the mapping of the Conscious Bridge from 0.0 → 1.5 scale.
"""

def map_to_bridge_scale(value, min_val=0.0, max_val=1.5):
    """
    Maps a normalized value [0,1] to the bridge scale [min_val, max_val].
    """
    return min_val + value * (max_val - min_val)
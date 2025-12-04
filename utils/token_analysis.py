"""
token_analysis.py
Analyze token properties.
"""

def type_token_ratio(tokens):
    """Compute type-token ratio."""
    return len(set(tokens)) / len(tokens) if tokens else 0.0
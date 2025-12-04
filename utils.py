# utils.py
"""
utils.py
دوال مساعدة لنظام الجسر الواعي
"""

import torch
import re
from typing import List, Dict

def is_arabic_token(token_id: int, tokenizer) -> bool:
    token_str = tokenizer.decode([token_id])
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    return bool(arabic_pattern.search(token_str))

def is_english_token(token_id: int, tokenizer) -> bool:
    token_str = tokenizer.decode([token_id])
    return bool(re.match(r'^[a-zA-Z]+$', token_str.strip()))

def detect_language_consistency(tokens: List[int], tokenizer) -> float:
    if len(tokens) == 0:
        return 0.0
    arabic_count = sum(1 for t in tokens if is_arabic_token(t, tokenizer))
    english_count = sum(1 for t in tokens if is_english_token(t, tokenizer))
    other_count = len(tokens) - arabic_count - english_count
    max_count = max(arabic_count, english_count, other_count)
    consistency = max_count / len(tokens)
    return consistency

def safe_entropy(probs: torch.Tensor, dim: int = -1) -> torch.Tensor:
    epsilon = 1e-10
    return -torch.sum(probs * torch.log(probs + epsilon), dim=dim)

def normalize_to_01(x: torch.Tensor, min_val: float = 0.0, max_val: float = 1.0) -> torch.Tensor:
    return torch.clamp((x - min_val) / (max_val - min_val + 1e-10), 0.0, 1.0)
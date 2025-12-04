# phi_calculator.py
"""
phi_calculator.py
خوارزمية حساب φ (الوعي) في الجسر الواعي
"""

import torch
from typing import Dict, Tuple, Optional
from utils import safe_entropy, normalize_to_01, detect_language_consistency

class PhiCalculator:
    def __init__(self, w_strength=0.35, w_attention=0.30, w_stability=0.25, w_context=0.10, language_centers: Optional[Dict[str, torch.Tensor]]=None):
        self.w1 = w_strength
        self.w2 = w_attention
        self.w3 = w_stability
        self.w4 = w_context
        total = self.w1 + self.w2 + self.w3 + self.w4
        assert abs(total - 1.0) < 1e-5, f"Weights must sum to 1.0, got {total}"
        self.language_centers = language_centers or {}

    def phi_strength(self, h_t: torch.Tensor) -> float:
        norm = torch.norm(h_t, p=2).item()
        phi_s = torch.tanh(torch.tensor(norm / 50.0)).item()
        return phi_s

    def phi_attention(self, attention_weights: torch.Tensor) -> float:
        entropy = safe_entropy(attention_weights, dim=-1)
        mean_entropy = entropy.mean().item()
        seq_len = attention_weights.shape[-1]
        max_entropy = torch.log(torch.tensor(float(seq_len))).item()
        phi_a = 1.0 - (mean_entropy / (max_entropy + 1e-10))
        phi_a = max(0.0, min(1.0, phi_a))
        return phi_a

    def phi_stability(self, h_t: torch.Tensor) -> float:
        if len(self.language_centers) < 2:
            return 0.5
        distances = {}
        for lang, center in self.language_centers.items():
            if center.shape[0] != h_t.shape[0]:
                continue
            dist = torch.norm(h_t - center, p=2).item()
            distances[lang] = dist
        if len(distances) < 2:
            return 0.5
        sorted_dists = sorted(distances.values())
        closest = sorted_dists[0]
        second_closest = sorted_dists[1]
        stability_ratio = (second_closest - closest) / (second_closest + 1e-10)
        phi_st = torch.tanh(torch.tensor(stability_ratio * 5.0)).item()
        return phi_st

    def phi_context(self, input_ids: torch.Tensor, tokenizer) -> float:
        tokens = input_ids.squeeze().tolist()
        if not isinstance(tokens, list):
            tokens = [tokens]
        context_length = len(tokens)
        length_score = min(context_length / 100.0, 1.0)
        unique_tokens = len(set(tokens))
        ttr = unique_tokens / (context_length + 1e-10)
        diversity_score = min(ttr * 2, 1.0)
        lang_consistency = detect_language_consistency(tokens, tokenizer)
        phi_c = (0.4 * length_score + 0.3 * diversity_score + 0.3 * lang_consistency)
        return phi_c

    def calculate(self, h_t: torch.Tensor, attention_weights: torch.Tensor, input_ids: torch.Tensor, tokenizer) -> Tuple[float, Dict[str, float]]:
        phi_s = self.phi_strength(h_t)
        phi_a = self.phi_attention(attention_weights)
        phi_st = self.phi_stability(h_t)
        phi_c = self.phi_context(input_ids, tokenizer)
        phi = (self.w1 * phi_s + self.w2 * phi_a + self.w3 * phi_st + self.w4 * phi_c)
        components = {
            "strength": phi_s,
            "attention": phi_a,
            "stability": phi_st,
            "context": phi_c,
            "total": phi
        }
        return phi, components
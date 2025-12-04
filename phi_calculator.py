"""
PhiCalculator for the Conscious Bridge Transformer
"""

import math
import torch
import torch.nn.functional as F
import numpy as np
from sklearn.cluster import KMeans

EPS = 1e-12

def sigmoid_scaled(x):
    return torch.tanh(x)

def phi_strength(h_t, clip_max=200.0):
    norm = torch.norm(h_t, p=2, dim=-1)
    phi_s = torch.tanh(norm / 50.0)
    return phi_s.clamp(0.0, 1.0)

def phi_attention(attention_weights):
    a = attention_weights
    if a.dim() == 4:
        entropy = - (a * (a + EPS).log()).sum(dim=-1).mean(dim=1)
        mean_entropy = entropy.mean(dim=-1)
        max_entropy = math.log(a.shape[-1] + EPS)
        phi_a = 1.0 - (mean_entropy / max_entropy)
        return phi_a.clamp(0.0, 1.0)
    elif a.dim() == 3:
        entropy = - (a * (a + EPS).log()).sum(dim=-1).mean(dim=0)
        mean_entropy = entropy.mean()
        max_entropy = math.log(a.shape[-1] + EPS)
        phi_a = 1.0 - (mean_entropy / max_entropy)
        return torch.tensor(phi_a).clamp(0.0, 1.0)
    else:
        raise ValueError("Unsupported attention shape")

def phi_stability(h_t, language_centers):
    if isinstance(language_centers, dict):
        centers = torch.stack(list(language_centers.values()), dim=0)
    else:
        centers = torch.tensor(language_centers)
    dists = torch.cdist(h_t, centers, p=2)
    sorted_vals, _ = torch.sort(dists, dim=1)
    closest = sorted_vals[:, 0]
    second = sorted_vals[:, 1] + EPS
    stability_ratio = (second - closest) / (second + EPS)
    phi_st = torch.tanh(stability_ratio * 5.0)
    return phi_st.clamp(0.0, 1.0)

def phi_context(input_ids, tokenizer, max_len=200):
    if isinstance(input_ids, torch.Tensor):
        tokens = input_ids.squeeze().tolist()
    else:
        tokens = list(input_ids)
    context_length = len(tokens)
    length_score = min(context_length / max_len, 1.0)
    unique_tokens = len(set(tokens))
    ttr = unique_tokens / (context_length + EPS)
    diversity_score = min(ttr * 2.0, 1.0)
    lang_consistency = 1.0
    try:
        text = tokenizer.decode(tokens)
        arabic_chars = sum(1 for c in text if '\u0600' <= c <= '\u06FF')
        if len(text) > 0:
            lang_consistency = arabic_chars / len(text)
            lang_consistency = min(max(lang_consistency, 0.0), 1.0)
    except Exception:
        lang_consistency = 0.5
    phi_c = 0.4 * length_score + 0.3 * diversity_score + 0.3 * lang_consistency
    return float(max(0.0, min(phi_c, 1.0)))

class PhiCalculator:
    def __init__(self,
                 w_strength=0.35,
                 w_attention=0.30,
                 w_stability=0.25,
                 w_context=0.10,
                 language_centers=None):
        self.w1 = w_strength
        self.w2 = w_attention
        self.w3 = w_stability
        self.w4 = w_context
        assert abs(self.w1 + self.w2 + self.w3 + self.w4 - 1.0) < 1e-6
        self.language_centers = language_centers

    @staticmethod
    def init_language_centers_from_corpus(embeddings, lang_labels, n_centers_per_lang=1, random_state=0):
        centers = {}
        unique_langs = sorted(set(lang_labels))
        for lang in unique_langs:
            idx = [i for i, l in enumerate(lang_labels) if l == lang]
            if len(idx) == 0:
                continue
            lang_embs = embeddings[idx]
            if n_centers_per_lang == 1:
                center = np.mean(lang_embs, axis=0)
            else:
                kmeans = KMeans(n_clusters=n_centers_per_lang, random_state=random_state).fit(lang_embs)
                center = kmeans.cluster_centers_.mean(axis=0)
            centers[lang] = torch.tensor(center, dtype=torch.float32)
        return centers

    def calculate(self, h_t, attention_weights, input_ids, tokenizer):
        if h_t.dim() == 1:
            h_t = h_t.unsqueeze(0)
        phi_s = phi_strength(h_t)
        phi_a = phi_attention(attention_weights)
        if isinstance(phi_a, torch.Tensor) and phi_a.dim() == 0:
            phi_a = phi_a.unsqueeze(0)
        phi_st = phi_stability(h_t, self.language_centers)
        phi_c_val = phi_context(input_ids, tokenizer)
        phi_c = torch.tensor([phi_c_val] * phi_s.shape[0], dtype=torch.float32)
        phi = (self.w1 * phi_s + self.w2 * phi_a + self.w3 * phi_st + self.w4 * phi_c)
        phi = phi.clamp(0.0, 1.0)
        components = {
            "strength": phi_s.detach().cpu().numpy().tolist(),
            "attention": (phi_a.detach().cpu().numpy().tolist() if isinstance(phi_a, torch.Tensor) else float(phi_a)),
            "stability": phi_st.detach().cpu().numpy().tolist(),
            "context": phi_c_val,
            "total": phi.detach().cpu().numpy().tolist()
        }
        if isinstance(components["total"], list) and len(components["total"]) == 1:
            components = {k: (v[0] if isinstance(v, list) else v) for k, v in components.items()}
            return float(phi.item()), components
        return phi, components

if __name__ == "__main__":
    print("PhiCalculator module ready.")
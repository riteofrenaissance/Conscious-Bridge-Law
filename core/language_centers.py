"""
language_centers.py
Utilities to manage language embedding centers.
"""

import torch
import numpy as np
from sklearn.cluster import KMeans

def compute_language_centers(embeddings, labels, n_clusters=1):
    """
    Compute cluster centers for each language.
    """
    centers = {}
    unique_langs = sorted(set(labels))
    for lang in unique_langs:
        idx = [i for i, l in enumerate(labels) if l == lang]
        lang_embs = embeddings[idx]
        if n_clusters == 1:
            center = np.mean(lang_embs, axis=0)
        else:
            kmeans = KMeans(n_clusters=n_clusters).fit(lang_embs)
            center = kmeans.cluster_centers_.mean(axis=0)
        centers[lang] = torch.tensor(center, dtype=torch.float32)
    return centers
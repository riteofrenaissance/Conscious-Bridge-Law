import numpy as np
from sklearn.cluster import KMeans
import torch

def compute_language_centers(embeddings, lang_labels, n_centers_per_lang=1, random_state=0):
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
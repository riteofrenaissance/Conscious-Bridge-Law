import torch
import numpy as np

EPS = 1e-12

def normalize_tensor(tensor, dim=-1):
    norm = torch.norm(tensor, p=2, dim=dim, keepdim=True)
    return tensor / (norm + EPS)

def cosine_similarity(a, b):
    a_norm = normalize_tensor(a)
    b_norm = normalize_tensor(b)
    return (a_norm * b_norm).sum(dim=-1)

def to_numpy(tensor):
    if isinstance(tensor, torch.Tensor):
        return tensor.detach().cpu().numpy()
    return np.array(tensor)
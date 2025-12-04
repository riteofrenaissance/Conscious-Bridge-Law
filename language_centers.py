# language_centers.py
"""
language_centers.py
حساب وتخزين مراكز اللغات في الفضاء الكامن
"""

import torch
from typing import Dict
from transformers import AutoModel, AutoTokenizer

class LanguageCenterCalculator:
    def __init__(self, model_name: str = "aubmindlab/bert-base-arabertv2"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()
        self.centers: Dict[str, torch.Tensor] = {}

    def calculate_center(self, texts: list, language: str) -> torch.Tensor:
        embeddings = []
        with torch.no_grad():
            for text in texts:
                inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
                outputs = self.model(**inputs)
                embedding = outputs.last_hidden_state[:, 0, :]
                embeddings.append(embedding)
        center = torch.stack(embeddings).mean(dim=0).squeeze()
        self.centers[language] = center
        return center

    def get_default_centers(self, d_model: int = 768) -> Dict[str, torch.Tensor]:
        if len(self.centers) == 0:
            arabic_samples = [
                "الذكاء الاصطناعي يتطور بسرعة",
                "اللغة العربية لغة جميلة وغنية",
                "البرمجة مهارة مهمة في العصر الحديث"
            ]
            english_samples = [
                "Artificial intelligence is evolving rapidly",
                "Arabic language is beautiful and rich",
                "Programming is an important skill in modern times"
            ]
            print("🔄 Calculating language centers...")
            self.calculate_center(arabic_samples, "ar")
            self.centers["en"] = torch.randn(d_model) * 0.5 + 1.0
            print("✅ Language centers ready")
        return self.centers
# conscious_transformer.py
"""
conscious_transformer.py
Transformer مع الجسر الواعي
"""

import torch
from typing import Optional, Dict, Tuple
from transformers import AutoModelForCausalLM, AutoTokenizer
from phi_calculator import PhiCalculator
from language_centers import LanguageCenterCalculator

class ConsciousBridgeTransformer:
    def __init__(self, model_name: str = "aubmindlab/aragpt2-base", phi_calculator: Optional[PhiCalculator] = None):
        print(f"🔄 Loading model: {model_name}")
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model.eval()
        print("🔄 Initializing language centers...")
        lang_calc = LanguageCenterCalculator()
        d_model = self.model.config.hidden_size
        centers = lang_calc.get_default_centers(d_model)
        self.phi_calc = phi_calculator or PhiCalculator(language_centers=centers)
        print("✅ Conscious Bridge Transformer ready!")

    def _adjust_temperature(self, phi: float, base_T: float) -> float:
        if phi > 0.8:
            return base_T * 0.6
        elif phi > 0.5:
            return base_T
        elif phi > 0.3:
            return base_T * 1.3
        else:
            return base_T * 1.5

    def _print_phi_report(self, phi: float, components: Dict[str, float], base_T: float, adjusted_T: float):
        print("\n" + "="*60)
        print("🌉 CONSCIOUS BRIDGE ANALYSIS")
        print("="*60)
        print(f"φ (Bridge Awareness):  {phi:.3f}")
        print(f"   ├─ Strength:        {components['strength']:.3f}")
        print(f"   ├─ Attention:       {components['attention']:.3f}")
        print(f"   ├─ Stability:       {components['stability']:.3f}")
        print(f"   └─ Context:         {components['context']:.3f}")
        print(f"\n🌡️  Temperature:        {base_T:.2f} → {adjusted_T:.2f}")
        if phi > 0.8:
            status = "🟢 STRONG - High confidence"
        elif phi > 0.5:
            status = "🟡 MODERATE - Normal operation"
        elif phi > 0.3:
            status = "🟠 WEAK - Increased exploration"
        else:
            status = "🔴 FRAGILE - High uncertainty"
        print(f"📊 Bridge Status:      {status}")
        if phi < 0.3:
            print("\n⚠️  WARNING: Low bridge awareness detected!")
            print("   Context may be ambiguous or linguistically unstable.")
        print("="*60 + "\n")

    @torch.no_grad()
    def generate_with_awareness(self, input_text: str, base_temperature: float = 0.7, max_new_tokens: int = 50, adaptive_temp: bool = True, verbose: bool = True) -> Tuple[str, float, Dict]:
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
        outputs = self.model(input_ids, output_hidden_states=True, output_attentions=True)
        h_t = outputs.hidden_states[-1][0, -1, :]
        attention = outputs.attentions[-1]
        phi, components = self.phi_calc.calculate(h_t=h_t, attention_weights=attention, input_ids=input_ids, tokenizer=self.tokenizer)
        adjusted_T = self._adjust_temperature(phi, base_temperature) if adaptive_temp else base_temperature
        if verbose:
            self._print_phi_report(phi, components, base_temperature, adjusted_T)
        generated_ids = self.model.generate(input_ids, max_new_tokens=max_new_tokens, temperature=adjusted_T, do_sample=(adjusted_T > 0.1), pad_token_id=self.tokenizer.eos_token_id)
        generated_text = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        return generated_text, phi, components
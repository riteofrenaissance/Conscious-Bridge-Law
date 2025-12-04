# engine/conscious_law.py

import torch
from core.phi_calculator import PhiCalculator
from engine.temperature_adapter import TemperatureAdapter
from engine.stability_monitor import StabilityMonitor

class ConsciousBridgeLaw:
    def __init__(self, model=None, tokenizer=None, phi_calculator=None):
        self.model = model
        self.tokenizer = tokenizer
        self.phi_calculator = phi_calculator or PhiCalculator()
        self.temp_adapter = TemperatureAdapter()
        self.stability_monitor = StabilityMonitor()
    
    def generate_with_awareness(self, input_text, base_temperature=0.7, max_new_tokens=50,
                                adaptive_temp=True, verbose=False):
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
        hidden_states = self.model(input_ids).last_hidden_state
        attention_weights = self.model(input_ids, output_attentions=True).attentions[-1]

        phi, components = self.phi_calculator.calculate(hidden_states, attention_weights, input_ids, self.tokenizer)

        temperature = base_temperature
        if adaptive_temp:
            temperature = self.temp_adapter.adapt_temperature(base_temperature, phi)

        output_ids = self.model.generate(input_ids, max_new_tokens=max_new_tokens, temperature=temperature)
        output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        if verbose:
            print(f"Input: {input_text}")
            print(f"Output: {output_text}")
            print(f"Phi: {phi}")
            print(f"Components: {components}")
            print(f"Temperature used: {temperature}")

        return output_text, phi, components
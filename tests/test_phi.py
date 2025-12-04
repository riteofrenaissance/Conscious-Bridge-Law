"""
test_phi.py
Unit test for PhiCalculator.
"""

import torch
from core.phi_calculator import PhiCalculator

def test_phi_calculation():
    phi_calc = PhiCalculator()
    h_t = torch.rand(1, 768)
    attention = torch.rand(1, 12, 10, 10)
    input_ids = list(range(10))
    phi, components = phi_calc.calculate(h_t, attention, input_ids, tokenizer=None)
    assert 0.0 <= phi <= 1.0
    print("Phi test passed:", phi, components)

if __name__ == "__main__":
    test_phi_calculation()
# 🌉 Conscious Bridge Law
**Transitional Geometry between Aristotelian and Platonic Logic in AI**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17814683.svg)](https://doi.org/10.5281/zenodo.17814683)
[![Stars](https://img.shields.io/github/stars/riteofrenaissance/Conscious-Bridge-Law?style=social)](https://github.com/riteofrenaissance/Conscious-Bridge-Law/stargazers)

*By Samir Baladi | December 3, 2025*

---

## 🎯 What is Conscious Bridge Law?

Instead of forcing AI to choose between:

- **Deterministic** (Aristotelian: T=0) 
- **Probabilistic** (Platonic: T=1.5)

We introduce a **third space**: The Conscious Bridge (T ∈ [0.4, 0.8])

Aristotle ←─── Conscious Bridge (φ) ───→ Plato T=0.0           T=0.6                 T=1.5 Certain         Aware                 Creative

### Key Innovation: φ (Phi)
**φ** measures the model's **awareness** of its position on the bridge:

- φ=0: Unconscious transition (random drift)
- φ=1: Fully conscious (controlled navigation)

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt

from engine.conscious_law import ConsciousBridgeLaw

# Initialize
model = ConsciousBridgeLaw()

# Generate with awareness
output, phi, components = model.generate_with_awareness(
    input_text="Artificial intelligence is evolving",
    base_temperature=0.7,
    adaptive_temp=True
)

print(f"Bridge Awareness (φ): {phi:.3f}")
print(f"Generated: {output}")


---

📊 φ Components

Component	Weight	Description

Strength	35%	Context representation power (‖hₜ‖)
Attention	30%	Attention mechanism clarity
Stability	25%	Language stability (distance from centers)
Context	10%	Input context quality



---

📂 Repository Structure

Conscious-Bridge-Law/
├── core/
│   ├── bridge_map.py
│   ├── bridge_dynamics.py
│   ├── phi_calculator.py
│   ├── language_centers.py
│   └── attention_metrics.py
├── engine/
│   ├── conscious_law.py
│   ├── temperature_adapter.py
│   └── stability_monitor.py
├── bos/
│   ├── identity_layer.py
│   ├── role_manager.py
│   └── state_manager.py
├── demos/
│   ├── arabic_context.py
│   ├── mixed_language.py
│   └── philosophical_queries.py
├── utils/
│   ├── token_analysis.py
│   └── metrics.py
├── tests/
│   └── test_phi.py
├── docs/                    → PDF and supporting files (CC-BY 4.0)
├── README.md                → Documentation + Badges
├── requirements.txt
├── CONTRIBUTING.md          → Contribution guidelines
├── .gitignore               → Excluded files
└── setup.py / pyproject.toml → Package installation


---

🎓 Citation

@software{baladi_2025_conscious_bridge,
  author       = {Baladi, Samir},
  title        = {{Conscious Bridge Law: Implementation}},
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17814683},
  url          = {https://doi.org/10.5281/zenodo.17814683}
}


---

⚖️ License

Code: MIT License

Papers & Docs: CC-BY 4.0


See LICENSE-MIT.txt and LICENSE-CC-BY.txt


---

🤝 Contributing

We welcome contributions! See CONTRIBUTING.md


---

🔗 Links

📄 Academic Publication (Zenodo)

💻 GitLab Mirror

📚 Full Documentation

📊 Visualizations



---

🌟 ## 📜 Release History

### v1.0.0 — December 4, 2025
- Initial release of Conscious Bridge Law
- Core Python code: `PhiCalculator` and `ConsciousBridgeLaw` classes
- Demo scripts and tests included
- Full documentation and README provided
- Licensed under MIT (code) + CC-BY 4.0 (docs)

---

### Planned Updates
- Add `setup.py` / `pyproject.toml` for pip installation
- Expand demos with real-world examples
- Add notebooks for φ calculation and visualization
- Improve README with interactive table of contents
- Include CONTRIBUTING.md (guidelines for collaboration)
- Publish package to PyPI / TestPyPI
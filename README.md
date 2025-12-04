# 🌉 Conscious-Bridge-Law
**Conscious Bridge Law in Artificial Intelligence**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![DOI](https://zenodo.org/badge/1109741482.svg)](https://doi.org/10.5281/zenodo.17814682)

---

## 📖 Overview

This project implements the **Conscious Bridge Law** on Transformer-based models, where:

- **T (Temperature):** Determines the model's position between deterministic (Aristotelian) and probabilistic (Platonic) modes.  
- **φ (Phi / Awareness):** Measures the "strength of the bridge," i.e., how aware the model is of its cognitive position.  
- **Dynamic Adjustment:** T adapts based on φ to improve generation quality.  

---

## 📂 Repository Structure

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
├── README.md  
└── requirements.txt  

- **docs/** → PDF and supporting files (CC-BY 4.0)  
- **Python scripts** → MIT License  
- **README.md** → Documentation  

---

## ⚖️ Licensing

- **PDF and research documents:** CC-BY 4.0  
- **Code files:** MIT License  

---

## 📌 Usage Notes

- Import `PhiCalculator` and `ConsciousBridgeLaw` in your pipelines.  
- Example scripts are provided in `demos/`.  
- Maintain folder structure for reproducibility.  
- CC-BY content requires proper attribution.  

---

## 📝 Example

```python
from engine.conscious_law import ConsciousBridgeLaw

model = ConsciousBridgeLaw()
output, phi, components = model.generate_with_awareness(
    input_text="Artificial intelligence is rapidly evolving",
    base_temperature=0.7,
    max_new_tokens=30,
    adaptive_temp=True,
    verbose=True
)
print("Generated text:", output)
print("Phi value:", phi)
print("Components:", components)
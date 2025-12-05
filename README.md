<p align="center">
  <img src="docs/bridge.png" alt="Conscious Bridge Law Logo" width="180"/>
</p>

<h1 align="center">🌉 Conscious Bridge Law</h1>
<p align="center"><em>Transitional Geometry between Aristotelian and Platonic Logic in AI</em></p>

**Transitional Geometry between Aristotelian and Platonic Logic in AI**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17814683.svg)](https://doi.org/10.5281/zenodo.17814683)
[![GitHub Stars](https://img.shields.io/github/stars/riteofrenaissance/Conscious-Bridge-Law?style=social)](https://github.com/riteofrenaissance/Conscious-Bridge-Law/stargazers)
[![GitLab Last Commit](https://img.shields.io/gitlab/last-commit/cyber-constitution/conscious-bridge/conscious-bridge-law)](https://gitlab.com/cyber-constitution/conscious-bridge/conscious-bridge-law)

By **Samir Baladi** | December 3, 2025


---

## 📖 Table of Contents

- Overview
- Quick Start
- Installation
- φ Components
- Usage
- Repository Structure
- Citation
- License
- Contributing
- Contact
- Links
- Release History

--

## 🎯 Overview

Instead of forcing AI to choose between:

- **Deterministic** (Aristotelian: T=0)
- **Probabilistic** (Platonic: T=1.5)

We introduce a **third space**: The Conscious Bridge (T ∈ [0.4, 0.8])

```
Aristotle ←─── Conscious Bridge (φ) ───→ Plato
T = 0.0          T = 0.6                T = 1.5
Certain          Aware                  Creative
```

**Key Innovation: φ (Phi)**

φ measures the model's awareness of its position on the bridge:

- φ = 0: Unconscious transition (random drift)  
- φ = 1: Fully conscious (controlled navigation)  

---

## 🚀 Quick Start

```python
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
```

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/riteofrenaissance/Conscious-Bridge-Law.git
cd Conscious-Bridge-Law

# Install dependencies
pip install -r requirements.txt

# Optional: Install in development mode
pip install -e .
```

Requirements: Python 3.8+, PyTorch 1.9+ or TensorFlow 2.5+

---

## 📊 φ Components

| Component  | Weight | Description |
|------------|--------|------------|
| Strength   | 35%    | Context representation power (‖hₜ‖) |
| Attention  | 30%    | Attention mechanism clarity |
| Stability  | 25%    | Language stability (distance from centers) |
| Context    | 10%    | Input context quality |

---

## 💻 Usage Examples

### Basic Usage

```python
from engine.conscious_law import ConsciousBridgeLaw

model = ConsciousBridgeLaw()
output, phi, _ = model.generate_with_awareness(
    input_text="The nature of consciousness",
    base_temperature=0.6
)
```

### Advanced: Monitoring φ

```python
import matplotlib.pyplot as plt

phi_history = []
for i in range(10):
    _, phi, _ = model.generate_with_awareness(
        input_text=f"Step {i}: AI evolution",
        base_temperature=0.5 + (i * 0.05)
    )
    phi_history.append(phi)

# Visualize φ evolution
plt.plot(phi_history, marker='o')
plt.xlabel('Iteration')
plt.ylabel('φ Value')
plt.title('Conscious Bridge Awareness Evolution')
plt.grid(True)
plt.show()
```

---

## 📂 Repository Structure

```


Conscious-Bridge-Law/
├── core/                    # Core algorithms
│   ├── bridge_map.py
│   ├── bridge_dynamics.py
│   ├── phi_calculator.py
│   ├── language_centers.py
│   └── attention_metrics.py
├── engine/                  # Main engine
│   ├── conscious_law.py
│   ├── temperature_adapter.py
│   └── stability_monitor.py
├── bos/                     # State management
│   ├── identity_layer.py
│   ├── role_manager.py
│   └── state_manager.py
├── demos/                   # Example scripts
│   ├── arabic_context.py
│   ├── mixed_language.py
│   ├── philosophical_queries.py
│   ├── web_demo.py                 # DeepSeek addition
│   ├── advanced_simulation.py      # DeepSeek addition
│   ├── multi_language_demo.py      # DeepSeek addition
│   └── data_analysis_demo.py       # DeepSeek addition
├── utils/                   # Utilities
│   ├── token_analysis.py
│   ├── metrics.py
│   ├── phi_logger.py               # DeepSeek addition
│   └── visualizer.py               # DeepSeek addition
├── tests/                   # Test suite
│   ├── test_phi.py
│   ├── test_bridge_map.py          # DeepSeek addition
│   ├── test_bridge_dynamics.py    # DeepSeek addition
│   ├── test_phi_calculator.py     # DeepSeek addition
│   └── test_conscious_law.py      # DeepSeek addition
├── docs/                    # Documentation and images
│   ├── bridge.png                  # Logo
│   ├── example_output.png
│   ├── architecture_diagram.png
│   ├── research_paper.md          # DeepSeek addition
│   └── tutorial.md                # DeepSeek addition
├── requirements.txt         # Dependencies
├── setup.py                  # Optional: Package installer
├── pyproject.toml           # Optional: Package configuration
├── LICENSE-MIT.txt          # MIT License
├── LICENSE-CC-BY.txt        # CC-BY License
├── CONTRIBUTING.md          # Contribution guidelines
├── .gitignore               # Ignore patterns for Git
└── README.md                # Main README

```

---

## 🎓 Citation

```bibtex
@software{baladi_2025_conscious_bridge,
  author       = {Baladi, Samir},
  title        = {{Conscious Bridge Law: Implementation}},
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17814683},
  url          = {https://doi.org/10.5281/zenodo.17814683}
}
```

---

## ⚖️ License

- Code: MIT License  
- Documentation & Papers: CC-BY 4.0  

See [LICENSE-MIT.txt](LICENSE-MIT.txt) and [LICENSE-CC-BY.txt](LICENSE-CC-BY.txt)

---

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository  
2. Create a feature branch  
3. Make your changes  
4. Submit a Pull Request  

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📬 Contact

Maintainer: **Samir Baladi**  
Email: riteofrenaissance@proton.me  
Issues: [GitHub Issues](https://github.com/riteofrenaissance/Conscious-Bridge-Law/issues)

---
🔗 **Links**

## Official Platforms

🌐 **PyPI Package:** https://pypi.org/project/conscious-bridge  
💻 **GitHub Repository:** https://github.com/riteofrenaissance/Conscious-Bridge-Law  
🔄 **GitLab Mirror:** https://gitlab.com/cyber-constitution/conscious-bridge  
📄 **Academic Paper:** https://doi.org/10.5281/zenodo.17814683  

---

## Community

⭐ **Star on GitHub:** Show your support!  
🍴 **Fork the Project:** Create your own version  
👥 **Join Discussion:** Share your thoughts and ideas  

---

## 📈 Release History

### **v1.0.4 (Latest) — December 2025**
- ✅ Torch optional — Works without PyTorch dependency  
- ✅ Improved package structure — Fixed import issues  
- ✅ Multiple installation options — Basic, AI, Full, Dev  
- ✅ Better error handling — Graceful fallbacks  
- ✅ Arabic language support — Enhanced multilingual capabilities  

### **v1.0.3 — December 2025**
- Enhanced package structure and imports  

### **v1.0.2 — December 2025**
- Initial improvements and bug fixes  

### **v1.0.1 — December 2025**
- First public release on PyPI  

### **v1.0.0 — December 2025**
- Initial concept and implementation  

---

## 🌟 Featured In
This project represents a new frontier in AI research, bridging philosophy and technology in unprecedented ways.

---

## 🙏 Acknowledgments

- Inspired by the philosophical works of **Aristotle and Plato**  
- Built upon modern neural network architectures and attention mechanisms  
- Supported by the open-source community and AI research community  
- Special thanks to all contributors and early adopters  

---

## 📢 Share This Project

https://img.shields.io/badge/Share-Twitter-1DA1F2?style=for-the-badge&logo=twitter  
https://img.shields.io/badge/Share-LinkedIn-0077B5?style=for-the-badge&logo=linkedin  

---

**"Bridging the gap between certainty and creativity in AI"** 🌉  
**Conscious Bridge Law — Where Philosophy Meets Artificial Intelligence**
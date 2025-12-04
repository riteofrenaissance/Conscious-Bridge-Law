#!/usr/bin/env python3
from setuptools import setup, find_packages
import os

# قراءة README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# قراءة المتطلبات
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="conscious-bridge-law",
    version="1.0.0",
    author="Samir Baladi",
    author_email="riteofrenaissance@proton.me",
    description="Transitional Geometry between Aristotelian and Platonic Logic in AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riteofrenaissance/Conscious-Bridge-Law",
    packages=find_packages(include=["core", "engine", "bos", "utils", "demos"]),
    package_data={
        "conscious_bridge_law": ["docs/*.png", "docs/*.md"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "full": [
            "torch>=1.9.0",
            "transformers>=4.12.0",
            "matplotlib>=3.5.0",
            "streamlit>=1.22.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "conscious-bridge=engine.conscious_law:main",
            "bridge-demo=demos.web_demo:main",
        ],
        "conscious_bridge.plugins": [
            "map_plugin=core.bridge_map:BridgeMap",
            "dynamics_plugin=core.bridge_dynamics:BridgeDynamics",
            "phi_plugin=core.phi_calculator:PhiCalculator",
        ],
    },
)
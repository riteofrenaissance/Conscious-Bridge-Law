from setuptools import setup, find_packages

setup(
    name="conscious-bridge-law",
    version="1.0.0",
    author="Samir Baladi",
    description="Transitional Geometry between Aristotelian and Platonic Logic in AI",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "matplotlib>=3.8.0"
    ],
    python_requires=">=3.8",
    include_package_data=True,
    license="MIT",
    url="https://github.com/riteofrenaissance/Conscious-Bridge-Law"
)
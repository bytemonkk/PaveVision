from setuptools import setup, find_packages

setup(
    name="PaveVision",
    version="1.0.0",
    author="Manoj Kumar Sunkara",
    description="AI-Powered Pavement Distress Detection and PCI Estimation System",
    packages=find_packages(),
    install_requires=[
        "ultralytics>=8.3.0",
        "torch>=2.0.0",
        "flask>=3.0.0",
        "opencv-python>=4.10.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.8.0",
        "scikit-learn>=1.4.0"
    ],
    python_requires=">=3.10",
)
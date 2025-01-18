# setup.py
from setuptools import setup, find_packages

setup(
    name="topsis_Akhil_102203565",
    version="1.0.0",
    description="A Python package for topsis(Technique for Order Prefrence by Similarity to ideal solution) algorithm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Akhil Goyal",
    author_email="goyalakhil06022004@gmail.com",
    url="https://github.com/yourusername/graphUtils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

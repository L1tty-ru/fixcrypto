from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="fixcrypto",
    version="0.8.0",
    description="Secure encryption library using Double XOR Cipher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Scaramouche",
    author_email="",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="encryption, crypto, security, xor, cipher",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=[
        "Pillow>=9.0.0",
        "numpy>=1.21.0",
        "qrcode>=7.3.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.0"],
        "test": ["pytest>=7.0"],
    },
    project_urls={
        "Bug Reports": "https://github.com/scaramouche/fixcrypto/issues",
        "Source": "https://github.com/scaramouche/fixcrypto",
    },
)
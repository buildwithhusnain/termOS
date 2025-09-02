from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="termos",
    version="1.1.0",
    author="TermOS Project",
    author_email="contact@termos.dev",
    description="Cross-platform terminal with network management features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/termos",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Terminals",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "termos=termos.main:main",
        ],
    },
    keywords="terminal, network, proxy, wifi, hotspot, file-sharing, cross-platform",
    project_urls={
        "Bug Reports": "https://github.com/username/termos/issues",
        "Source": "https://github.com/username/termos",
        "Documentation": "https://github.com/username/termos/blob/main/README.md",
    },
)
#!/usr/bin/env python3
"""Setup configuration for AWESOME_OKAPI_V2"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="awesome_okapi_v2",
    version="2.0.0",
    author="Ian Carter Kulani, MSc",
    description="Cybersecurity Command & Control Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awesome-okapi/awesome-okapi-v2",
    project_urls={
        "Bug Tracker": "https://github.com/awesome-okapi/awesome-okapi-v2/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "certifi>=2024.12.14",
        "charset-normalizer>=3.4.0",
        "idna>=3.10",
        "requests>=2.32.3",
        "urllib3>=2.3.0",
        "cryptography>=41.0.7",
        "pycryptodome>=3.20.0",
        "paramiko>=3.4.0",
        "scapy>=2.5.0",
        "dnspython>=2.6.1",
        "whois>=0.9.4",
        "pyshorteners>=1.0.1",
        "Flask>=3.0.0",
        "Flask-SocketIO>=5.3.6",
        "Flask-CORS>=4.0.0",
        "python-socketio>=5.10.0",
        "discord.py>=2.3.2",
        "telethon>=1.34.0",
        "slack-sdk>=3.27.0",
        "pywhatkit>=5.4",
        "pynput>=1.7.6",
        "pyautogui>=0.9.54",
        "pyperclip>=1.8.2",
        "pygetwindow>=0.0.9",
        "matplotlib>=3.8.2",
        "seaborn>=0.13.1",
        "numpy>=1.26.4",
        "psutil>=5.9.6",
        "qrcode>=7.4.2",
        "Pillow>=10.3.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.1",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "awesome-okapi=awesome_okapi_v2:main",
        ],
    },
)
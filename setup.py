"""
Setup script for the name2date package.
"""

from setuptools import setup, find_packages
import os

# Read the contents of the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Get version from __init__.py
with open(os.path.join("name2date", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[1].strip(" '\"")
            break
    else:
        version = "0.1.0"

setup(
    name="name2date",
    version=version,
    description="Update Google Pixel video/photo modification dates based on their filenames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Konstantin Chaika",
    author_email="pro100kot14@gmail.com",
    url="https://github.com/kochaika/name2date",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Video",
        "Topic :: Utilities",
    ],
    keywords="video, image, date, time, metadata, file, modification, google pixel",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "name2date=name2date.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/kochaika/name2date/issues",
        "Source": "https://github.com/kochaika/name2date",
    },
)

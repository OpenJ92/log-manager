from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="log-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for managing logs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OpenJ92/log-manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)


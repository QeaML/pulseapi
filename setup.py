import setuptools
from pulseapi import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pulseapi",
    version=__version__,
    author="qeaml",
    author_email="qeaml@wp.pl",
    description="qeaml's wrapper for WhatPulse's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QeaML/pulseapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	license='MIT',
    python_requires='>=3.6',
	install_requires=['aiohttp'],
)
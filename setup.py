from setuptools import setup
import re
import os
import sys


setup(
    name="licorice",
    version="0.0.1",
    python_requires=">3.6.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url=None,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="licorice - vibrant string color additions.",
    packages=[
        "licorice",
    ],
    
    install_requires=[
	"numpy>=1.21.4",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)

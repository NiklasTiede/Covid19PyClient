#!/usr/bin/env python
"""The setup script."""
import pathlib

from setuptools import find_packages
from setuptools import setup

from src.covid19pyclient import __api_src__
from src.covid19pyclient import __author__
from src.covid19pyclient import __email__
from src.covid19pyclient import __version__


setup(
    name='covid19pyclient',
    version=__version__,
    author=__author__,
    author_email=__email__,
    license="MIT license",
    url='https://github.com/NiklasTiede/covid19pyclient',
    description=f"A Python Wrapper around the COVID-19 API {__api_src__!r}.",
    long_description=pathlib.Path("pypi_description.md").read_text(encoding="utf-8"),
    project_urls={
        'Documentation': 'https://covid19pyclient.readthedocs.io/en/latest/',
        'Source Code': 'https://github.com/NiklasTiede/covid19pyclient',
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.21.0",
    ],
    extras_require={         # pip install .[dev]
        "dev": [
            "pytest",
            "pytest-cov",
            "tox",
            "pre-commit",
        ],
    },
    platforms="any",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

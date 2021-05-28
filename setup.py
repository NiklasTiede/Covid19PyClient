#!/usr/bin/env python
"""The setup script."""
import pathlib

from setuptools import find_packages
from setuptools import setup

from covid19pyclient import __api_src__
from covid19pyclient import __author__
from covid19pyclient import __email__
from covid19pyclient import __version__

setup(
    name='covid19pyclient',
    version=__version__,
    url='https://github.com/NiklasTiede/covid19pyclient',
    author=__author__,
    author_email=__email__,
    license="MIT license",
    python_requires='>=3.6',
    description=f"A Python Wrapper around the COVID-19 API {__api_src__!r}.",
    long_description=pathlib.Path("pypi_description.md").read_text(encoding="utf-8"),
    # install_requires=requirements,
    include_package_data=True,
    keywords='covid19pyclient',
    # packages=find_packages(include=['covid19pyclient', 'covid19pyclient.*']),
    packages=find_packages(where="covid19pyclient"),
    setup_requires='pytest-runner',
    test_suite='tests',
    tests_require='pytest>=3',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

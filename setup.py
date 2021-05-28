#!/usr/bin/env python
"""The setup script."""
import pathlib

from setuptools import find_packages
from setuptools import setup

# from covid19pyclient import __api_src__
# from covid19pyclient import __author__
# from covid19pyclient import __email__
# from covid19pyclient import __version__


setup(
    name='covid19pyclient',
    version='1.0.0',
    url='https://github.com/NiklasTiede/covid19pyclient',
    author='Niklas Tiede',
    author_email='niklastiede2@gmail.com',
    license="MIT license",
    python_requires='>=3.6',
    description="A Python Wrapper around the COVID-19 API 'https://github.com/marlon360/rki-covid-api'.",
    long_description=pathlib.Path("pypi_description.md").read_text(encoding="utf-8"),
    install_requires=[
        "requests>=2.21.0",
    ],
    project_urls={
        'Documentation': '',    # TODO enter readthedocs url
        'Source Code': 'https://github.com/NiklasTiede/covid19pyclient',
    },
    # include_package_data=True,
    # keywords='covid19pyclient',
    # packages=find_packages(where="covid19pyclient"),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "tox",
            "pre-commit",
        ],
    },
    platforms="any",
    # setup_requires='pytest-runner',
    # test_suite='tests',
    # tests_require='pytest>=3',
    # zip_safe=False,
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

#!/usr/bin/env python
"""The setup script."""
import pathlib
import re
from typing import Any
from typing import Union

from setuptools import find_packages
from setuptools import setup


def get_value(variable: str) -> Union[str, Any]:
    """ Direct import of metadata would invoke a ModuleNotFoundError for 3rd party package
    libraries when installing this project for development.
    """
    content = pathlib.Path("src/covid19pyclient/__init__.py").read_text(encoding="utf-8")
    pattern = f'^{variable} = [\'"]([^\'\"]*)[\'"]'
    raw_s = r'{}'.format(pattern)
    p = re.compile(raw_s, re.M)
    return p.search(content).group(1)  # type: ignore


setup(
    name='covid19pyclient',
    version=get_value('__version__'),
    author=get_value('__author__'),
    author_email=get_value('__email__'),
    license="MIT license",
    url='https://github.com/NiklasTiede/covid19pyclient',
    description=f"A Python Wrapper around the COVID-19 API {get_value('__api_src__')!r}.",
    long_description=pathlib.Path("pypidocs.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
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
    extras_require={         # pip install -e .[dev]
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

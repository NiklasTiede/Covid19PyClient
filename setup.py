#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import pathlib


requirements = [ ]

setup(
    author="Niklas Tiede",
    author_email='niklastiede2@gmail.com',
    python_requires='>=3.6',
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
    description="A Python Wrapper around the COVID-19 API.",
    install_requires=requirements,
    license="MIT license",
    long_description=pathlib.Path("pypi_description.md").read_text(encoding="utf-8"),
    include_package_data=True,
    keywords='covid19pyclient',
    name='covid19pyclient',
    packages=find_packages(include=['covid19pyclient', 'covid19pyclient.*']),
    setup_requires='pytest-runner',
    test_suite='tests',
    tests_require='pytest>=3',
    url='https://github.com/NiklasTiede/covid19pyclient',
    version='0.1.0',
    zip_safe=False,
)

#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import pathlib


setup(
    name='covid19pyclient',
    version='0.1.0',
    url='https://github.com/NiklasTiede/covid19pyclient',
    author="Niklas Tiede",
    author_email='niklastiede2@gmail.com',
    license="MIT license",
    python_requires='>=3.6',
    description="A Python Wrapper around the COVID-19 API.",
    long_description=pathlib.Path("pypi_description.md").read_text(encoding="utf-8"),
    # install_requires=requirements,
    include_package_data=True,
    keywords='covid19pyclient',
    packages=find_packages(include=['covid19pyclient', 'covid19pyclient.*']),
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

#!/usr/bin/env python
"""Tests for `covid19pyclient` package."""
import time

import pytest

from src.covid19pyclient import CovidData


def test_germany_total():
    """Test if method returns expected data from the API endpoint."""
    # time.sleep(4)
    covid = CovidData()
    data = covid.germany_total()
    values = [
        ('cases', int),
        ('casesPer100k', float),
        ('casesPerWeek', int),
        ('deaths', int),
        ('delta', dict),
        ('meta', dict),
        ('recovered', int),
        ('weekIncidence', float)
        ]
    for key, value in values:
        print(key, data[key])
        assert type(data[key]) is value

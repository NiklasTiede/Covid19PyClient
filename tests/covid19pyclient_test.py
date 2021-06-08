#!/usr/bin/env python
"""Tests for `covid19pyclient` package."""
import time

from src.covid19pyclient import CovidData


def test_germany_total():
    """Test if method returns expected data from the API endpoint."""
    time.sleep(4)
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
        assert type(data[key]) is value


def test_germany_timeseries():
    """Test if method returns expected data from the API endpoint."""
    time.sleep(4)
    covid = CovidData()
    data = covid.germany_timeseries(days_limit=5, selected_type='deaths')['data']
    values = [
        ('deaths', int),
        ('date', str),
    ]
    for key, value in values:
        assert type(data[-1][key]) is value
    assert len(data) == 5

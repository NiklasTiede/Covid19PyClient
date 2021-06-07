
<p align="center">
  <img  alt="covid19pyclient" align="center" width="350" src="docs/covidclient.jpg" />
   <h3 align="center">A Thin Wrapper for the API of the Robert Koch Institute, Germany.</h3>
<p>


---

<p id="Badges" align="center">
  <!-- <a alt="Platform" href="https://pypi.org/project/covid19pyclient/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/covid19pyclient">
  </a> -->
  <a alt="GH actions" href="https://github.com/NiklasTiede/covid19pyclient/actions">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/NiklasTiede/covid19pyclient/Continuos%20Integration">
  </a>
  <!-- <a alt="GH Release" href="https://github.com/NiklasTiede/covid19pyclient/releases">
    <img src="https://img.shields.io/github/v/release/NiklasTiede/covid19pyclient" />
  </a> -->
  <a alt="Codecov" href="https://app.codecov.io/gh/NiklasTiede/covid19pyclient">
    <img src="https://img.shields.io/codecov/c/github/NiklasTiede/covid19pyclient" />
  </a>
</p>

<p align="center">
  <a alt="readthedocs documentation" href="https://covid19pyclient.readthedocs.io/en/latest/">Documentation</a>
  •
  <a alt="matplotlib plot examples" href="https://github.com/NiklasTiede/COVID19-API-PythonClient/tree/main/examples">Plot Examples</a>
  <!-- •
  <a alt="RKI API source code" href="https://github.com/marlon360/rki-covid-api">Covid API src</a> -->
<p>


<!-- PYPI-DOCS:START -->

# Example

```python
import json
from covid19pyclient import CovidData

covid = CovidData()
data = covid.germany_total()

print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
```

```yaml
{
    "cases": 3682911,
    "casesPer100k": 4428.3475391975035,
    "casesPerWeek": 29248,
    "deaths": 88595,
    "delta": {
        "cases": 1785,
        "deaths": 153,
        "recovered": 11714
    },
    "meta": {
        "contact": "Marlon Lueckert (m.lueckert@me.com)",
        "info": "https://github.com/marlon360/rki-covid-api",
        "lastCheckedForUpdate": "2021-06-01T08:17:40.241Z",
        "lastUpdate": "2021-05-31T23:00:00.000Z",
        "source": "Robert Koch-Institut"
    },
    "r": {
        "date": "2021-05-27T00:00:00.000Z",
        "value": 0.91
    },
    "recovered": 3498382,
    "weekIncidence": 35.16791712491793
}
```

# Featured Data

- Total number of COVID-19 related cases, deaths, incidence, recovered (country, by state, by district, by demographics)
- Timeseries data (country, districts, vaccinations, tests)
- And data derived therefrom

# Installation

You can install `covid19pyclient` with pip.

```console
$ pip install covid19pyclient
```

Alternatively, you can download and install `covid19pyclient` from github:

```console
$ pip install git+https://github.com/NiklasTiede/Covid19PyClient
```

# How to use

`CovidData`'s class methods return the requested as dictionary.

```python
from covid19pyclient import CovidData

covid = CovidData()
```
Here's a list of all the methods which can be used to access different data about COVID-19 in germany:

```python
covid.germany_total()
covid.germany_timeseries()
covid.germany_by_agegroups()

covid.districts_total()
covid.districts_timeseries()

covid.states_total()
covid.states_by_agegroups()

covid.vaccinations_total()
covid.vaccinations_timeseries()

covid.testing_timeseries()
```

For more information about these function, see [Documentation](https://covid19pyclient.readthedocs.io/en/latest/).

<!-- PYPI-Docs:END -->

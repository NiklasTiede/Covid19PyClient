
<p align="center">
  <img  alt="covid19pyclient" align="center" width="400" src="docs/covidclient.jpg" />
<p>

<p align="center">
   <h3 align="center">A Thin Python Wrapper for the <a alt="rki covid api" href="https://api.corona-zahlen.org/docs/">COVID-19 API</a> of the Robert Koch Institute, Germany.</h3>
<p>

<<<<<<< HEAD
<p id="Badges" align="center">
  <!-- <a alt="Platform" href="https://pypi.org/project/covid19pyclient/">
=======
---
    
<!-- <p id="Badges" align="center">
  <a alt="Platform" href="https://pypi.org/project/covid19pyclient/">
>>>>>>> db22313e36b5a2f204114c73b63d7848bbbf242b
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/covid19pyclient">
  </a> -->
  <a alt="GH actions" href="https://github.com/NiklasTiede/covid19pyclient/actions">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/NiklasTiede/covid19pyclient/Continuos%20Integration">
  </a>
  <!-- <a alt="GH Release" href="https://github.com/NiklasTiede/covid19pyclient/releases">
    <img src="https://img.shields.io/github/v/release/NiklasTiede/covid19pyclient" />
  </a>
  <a alt="Codecov" href="https://app.codecov.io/gh/NiklasTiede/covid19pyclient">
    <img src="https://img.shields.io/codecov/c/github/NiklasTiede/covid19pyclient" />
  </a> -->
</p>


<p align="center">
  <a alt="readthedocs documentation" href="">Documentation</a>
  •
  <a alt="matplotlib plot examples" href="">Plot Examples</a>
  •
  <a alt="RKI API source code" href="">Covid API src</a>
<p>


<!-- PYPI-DOCS:START -->

# Example

```python
import json
from covid19pyclient import CovidData

covid = CovidData()
data = covid.germany_total()

print(json.dumps(data, sort_keys=True, indent=4))
```

```json
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


# Contents
- [Featured Data](#features)
- [Installation](#installation)
- [How to use covid19pyclient](#how-to-use-covid19pyclient)

# Features



# Installation

You can install COVID-19 API Python Client with pip.

```python
$ pip install covid19pyclient
```

# How to use covid19pyclient




<!-- PYPI-Docs:END -->

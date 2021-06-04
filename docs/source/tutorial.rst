How to Use
==========

This guide can help you start working with ``covid19pyclient``.

Retrieving Data
---------------

The class ``CovidData`` contains the methods which will return all data from the Covid API::

    from covid19pyclient import CovidData

    covid = CovidData()

The data are returned as dictionaries. Here's an example::

    data = covid.germany_total()

    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))

output::

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

.. note::
   To convert the datetime strings of the API responses into Python datetime objects more conveniently this module contains a ``.datereader()`` function.

----------

Categories
----------

Depending on the kind of data you want to retrieve, the wrapper provides 10 methods::

    [method for method in dir(CovidData) if '__' not in method]

    [
    'districts_timeseries',
    'districts_total',
    'germany_by_agegroups',
    'germany_timeseries',
    'germany_total',
    'states_by_agegroups',
    'states_total',
    'testing_timeseries',
    'vaccinations_timeseries',
    'vaccinations_total'
    ]

These methods can be divided into 5 categories:

.. list-table::
   :widths: 25 30 100
   :header-rows: 1

   * - Prefix / Category
     - Meaning
     - Provided Data
   * - ``germany_``
     - Data on the whole country (germany)
     - accumulated, timeseries, age-groups
   * - ``states_``
     - Data are spatially divided into 16 states
     - accumulated, timeseries, age-groups
   * - ``districts_``
     - Data spatially divided into 412 districts
     - accumulated, timeseries, age-groups
   * - ``vaccinations_``
     - Data on vaccinations
     - accumulated, timeseries
   * - ``testing_``
     - Data on testing
     - accumulated, timeseries

In the next chapter you will see how to use the methods and how the returned data will look like.

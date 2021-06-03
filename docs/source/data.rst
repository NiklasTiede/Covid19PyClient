Available Data
==============

In the following all methods which return API data are explained in detail. Each API response contains a meta-key which provides information about the maintainer of the API and when it was updated at last. The data can be retrieved by calling the methods of the ``CovidData`` class.

All data from germany as a whole. You can choose between 4 types (cases, deaths, incidence and recovered).
state in STATE, days limit/weeks limit integers::

    from covid19pyclient import CovidData

    covid = CovidData()

    # Germany
    covid.germany_total()
    covid.germany_timeseries(days_limit=3, selected_type='cases')
    covid.germany_by_agegroups()

    # States
    covid.states_total(state='BY')
    covid.states_by_agegroups(state='BY')

    # Districts
    covid.districts_total()
    covid.districts_timeseries(days_limit=5, selected_type='deaths')

    # Vaccinations
    covid.vaccinations_total()
    covid.vaccinations_timeseries(days_limit=3)

    # Testing
    covid.testing_timeseries(weeks_limit=2)

You can limit the retrieved data to certain types and locations. Furthermore, the number of timeseries datapoints can be limited to the last x values (see above).
In the following all allowed types of data and states are listed::

    from covid19pyclient import TYPES, STATES

    print(TYPES)
    ['cases', 'incidence', 'deaths', 'recovered']

    print(STATES)
    ['BW', 'BY', 'BE', 'BB', 'HB', 'HH', 'HE', 'MV', 'NI', 'NW', 'RP', 'SL', 'SN', 'ST', 'SH', 'TH']



Germany
-------

These methods return data about the whole country.

total::

    data = covid.germany_total()

output::

    {
    "cases": 3692468,
    "casesPer100k": 4439.838915837371,
    "casesPerWeek": 28331,
    "deaths": 88940,
    "delta": {
        "cases": 4640,
        "deaths": 166,
        "recovered": 8904
    },
    "meta": {
        "contact": "Marlon Lueckert (m.lueckert@me.com)",
        "info": "https://github.com/marlon360/rki-covid-api",
        "lastCheckedForUpdate": "2021-06-03T11:19:19.187Z",
        "lastUpdate": "2021-06-02T23:00:00.000Z",
        "source": "Robert Koch-Institut"
    },
    "r": {
        "date": "2021-05-29T00:00:00.000Z",
        "value": 0.87
    },
    "recovered": 3518551,
    "weekIncidence": 34.065312502258266
    }

-----

timeseries ::

    covid.germany_timeseries(days_limit=3, selected_type='deaths')

output::

    [
    {
        "date": "2021-05-31T00:00:00.000Z",
        "deaths": 6
    },
    {
        "date": "2021-06-01T00:00:00.000Z",
        "deaths": 4
    },
    {
        "date": "2021-06-02T00:00:00.000Z",
        "deaths": 3
    }
    ]




text::

    data.





text::

    data.






text::

    data.












States
------

covid.states_total()
covid.states_by_agegroups()

Data from each state



text::

    data.




Districts
---------

covid.districts_total()
covid.districts_timeseries()




text::

    data.



Vaccinations
------------

covid.vaccinations_total()
covid.vaccinations_timeseries()


text::

    data.






Testing
-------

covid.testing_timeseries(5)

text::

    data.

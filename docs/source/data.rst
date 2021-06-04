Available Data
==============

In the following all methods which return API data are explained in detail. Each API response contains a meta-key which provides information about the maintainer of the API and when it was updated at last. All data can be retrieved by calling the methods of the ``CovidData`` class::

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
    covid.districts_total(ag='09184')
    covid.districts_timeseries(ag='09184', days_limit=10, selected_type='recovered')

    # Vaccinations
    covid.vaccinations_total()
    covid.vaccinations_timeseries(days_limit=3)

    # Testing
    covid.testing_timeseries(weeks_limit=2)

Retrieved data can be limited to certain types (cases, deaths, incidence, recovered) and geolocations (districts, states).
Furthermore, the datapoints of a timeseries can be limited.
In the following all allowed types of data and states are listed::

    from covid19pyclient import TYPES, STATES, AGS

    print(TYPES)
    ['cases', 'incidence', 'deaths', 'recovered']

    print(STATES)
    ['BW', 'BY', 'BE', 'BB', 'HB', 'HH', 'HE', 'MV', 'NI', 'NW', 'RP', 'SL', 'SN', 'ST', 'SH', 'TH']

    print(AGS)
    {'01001': 'Flensburg',
    '01002': 'Kiel',
    '01003': 'Lübeck',
    '01004': 'Neumünster',
    '01051': 'Dithmarschen',
    '01053': 'Herzogtum Lauenburg',
    '01054': 'Nordfriesland',
    '01055': 'Ostholstein',
    '01056': 'Pinneberg',
    '01057': 'Plön',
    ...


-----------

Germany
-------

These methods return data about the whole country. The first one returns the total number of current cases/deaths/recovered people in Germany::

    data = covid.germany_total()
    print(data)

Output::

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

----------

The API lets us also retrieve data about either ``cases``, ``deaths``, ``incidence`` or ``recovered`` patients over time.
By default the selected_type is 'cases'. We can limit the number of datapoints to the latest ``x`` number of datapoints.
By default all recorded datapoints are retrieved::

    data = covid.germany_timeseries(days_limit=3, selected_type='deaths')
    print(data)

Output::

    [
    {
        "date": "2021-05-30T00:00:00.000Z",
        "deaths": 2
    },
    {
        "date": "2021-05-31T00:00:00.000Z",
        "deaths": 6
    },
    {
        "date": "2021-06-01T00:00:00.000Z",
        "deaths": 5
    },
    {
        "date": "2021-06-02T00:00:00.000Z",
        "deaths": 3
    },
    {
        "date": "2021-06-03T00:00:00.000Z",
        "deaths": 2
    }
    ]


----------


We also have an API endpoint on demographic data. On this way all the data are broken down by age corhorts and gender::

    data = covid.germany_by_agegroups()['data']
    print(data)

Output::

    {
    "A00-A04": {
        "casesFemale": 45189,
        "casesFemalePer100k": 2341.8,
        "casesMale": 48689,
        "casesMalePer100k": 2396.5,
        "deathsFemale": 6,
        "deathsFemalePer100k": 0.3,
        "deathsMale": 2,
        "deathsMalePer100k": 0.1
    },
    "A05-A14": {
        "casesFemale": 127100,
        "casesFemalePer100k": 3520.9,
        "casesMale": 139283,
        "casesMalePer100k": 3646.2,
        "deathsFemale": 3,
        "deathsFemalePer100k": 0.1,
        "deathsMale": 3,
        "deathsMalePer100k": 0.1
    },
    "A15-A34": {
        "casesFemale": 535381,
        "casesFemalePer100k": 5821.7,
        "casesMale": 543470,
        "casesMalePer100k": 5477.7,
        "deathsFemale": 61,
        "deathsFemalePer100k": 0.7,
        "deathsMale": 111,
        "deathsMalePer100k": 1.1
    },
    "A35-A59": {
        "casesFemale": 722247,
        "casesFemalePer100k": 5028.9,
        "casesMale": 681338,
        "casesMalePer100k": 4680.4,
        "deathsFemale": 1094,
        "deathsFemalePer100k": 7.6,
        "deathsMale": 2596,
        "deathsMalePer100k": 17.8
    },
    "A60-A79": {
        "casesFemale": 270503,
        "casesFemalePer100k": 2843.2,
        "casesMale": 269030,
        "casesMalePer100k": 3149,
        "deathsFemale": 9015,
        "deathsFemalePer100k": 94.8,
        "deathsMale": 17211,
        "deathsMalePer100k": 201.5
    },
    "A80+": {
        "casesFemale": 189563,
        "casesFemalePer100k": 5389.5,
        "casesMale": 97106,
        "casesMalePer100k": 4487.6,
        "deathsFemale": 32020,
        "deathsFemalePer100k": 910.4,
        "deathsMale": 26727,
        "deathsMalePer100k": 1235.1
    }
    }


------



States
------

Germany has 16 federal states. The API allows us to request accumulated data of each state.
We have to pass the 2-letter code of the respective state as argument into the method. By default all states are returned.
In the following example data about the state bavaria (bayern) were obtained::

    data = covid.states_total(state='BY')['data']
    print(data)

Output::

    {
    "BY": {
        "abbreviation": "BY",
        "cases": 641339,
        "casesPer100k": 4886.4902969103305,
        "casesPerWeek": 3806,
        "deaths": 14996,
        "deathsPerWeek": 8,
        "delta": {
        "cases": 430,
        "deaths": 6,
        "recovered": 1196
        },
        "id": 9,
        "name": "Bayern",
        "population": 13124737,
        "recovered": 614949,
        "weekIncidence": 28.998676316333043
    }
    }



----------


Furthermore, we can retrieve demographic data for each state::

    data = covid.states_by_agegroups(state='BY')['data']
    print(data)


Output::

    {
    "BY": {
        "A00-A04": {
        "casesFemale": 7859,
        "casesFemalePer100k": 2520.1,
        "casesMale": 8277,
        "casesMalePer100k": 2530.5,
        "deathsFemale": 1,
        "deathsFemalePer100k": 0.3,
        "deathsMale": 0,
        "deathsMalePer100k": 0
        },
        "A05-A14": {
        "casesFemale": 21750,
        "casesFemalePer100k": 3851.9,
        "casesMale": 24014,
        "casesMalePer100k": 4028.2,
        "deathsFemale": 2,
        "deathsFemalePer100k": 0.4,
        "deathsMale": 0,
        "deathsMalePer100k": 0
        },
        "A15-A34": {
        "casesFemale": 93225,
        "casesFemalePer100k": 6202.4,
        "casesMale": 100645,
        "casesMalePer100k": 6170.1,
        "deathsFemale": 11,
        "deathsFemalePer100k": 0.7,
        "deathsMale": 16,
        "deathsMalePer100k": 1
        },
        "A35-A59": {
        "casesFemale": 120629,
        "casesFemalePer100k": 5244,
        "casesMale": 120254,
        "casesMalePer100k": 5147.9,
        "deathsFemale": 158,
        "deathsFemalePer100k": 6.9,
        "deathsMale": 412,
        "deathsMalePer100k": 17.6
        },
        "A60-A79": {
        "casesFemale": 44411,
        "casesFemalePer100k": 3112.7,
        "casesMale": 45595,
        "casesMalePer100k": 3517.6,
        "deathsFemale": 1477,
        "deathsFemalePer100k": 103.5,
        "deathsMale": 2769,
        "deathsMalePer100k": 213.6
        },
        "A80+": {
        "casesFemale": 30436,
        "casesFemalePer100k": 5963.1,
        "casesMale": 15634,
        "casesMalePer100k": 4869,
        "deathsFemale": 5645,
        "deathsFemalePer100k": 1106,
        "deathsMale": 4403,
        "deathsMalePer100k": 1371.3
        }
    }
    }


-----------------


Districts
---------

Germany has 412 districts (Kreise und kreisfreie Städte).
The data are further splitted into these districts.
They are sorted by the first 5-digits (Kreischlüssel) of their 8-digit Community identification number (amtlicher Gemeindeschlüssel)::

    data = covid.districts_total(ag=14713)['data']
    print(data)

Output::

    {
    "09162": {
        "ags": "09162",
        "cases": 72733,
        "casesPer100k": 4900.399265340992,
        "casesPerWeek": 388,
        "county": "SK München",
        "deaths": 1242,
        "deathsPerWeek": 1,
        "delta": {
        "cases": 32,
        "deaths": 0,
        "recovered": 134
        },
        "name": "München",
        "population": 1484226,
        "recovered": 70220,
        "state": "Bayern",
        "stateAbbreviation": "BY",
        "weekIncidence": 26.14157143184394
    }
    }


----------


Additionally, we can retrieve a timeseries of each district.
When no days_limit argument is provided all recorded datapoints are returned by the API::

    data = covid.districts_timeseries(days_limit=10, ag='09184')['data']
    print(data)

Output::

    {
    "09184": {
        "ags": "09184",
        "history": [
        {
            "cases": 8,
            "date": "2021-05-30T00:00:00.000Z"
        },
        {
            "cases": 9,
            "date": "2021-05-31T00:00:00.000Z"
        },
        {
            "cases": 14,
            "date": "2021-06-01T00:00:00.000Z"
        },
        {
            "cases": 12,
            "date": "2021-06-02T00:00:00.000Z"
        },
        {
            "cases": 3,
            "date": "2021-06-03T00:00:00.000Z"
        }
        ],
        "name": "LK München"
    }
    }


--------------


Vaccinations
------------


The API returns also data about the total number of vaccinations::

    data = covid.vaccinations_total()['data']
    print(data)


Output::

    {
    "administeredVaccinations": 52779769,
    "delta": 511668,
    "indication": {
        "age": null,
        "job": null,
        "medical": null,
        "nursingHome": null,
        "secondVaccination": {
        "age": null,
        "job": null,
        "medical": null,
        "nursingHome": null
        }
    },
    "quote": 0.43841572621526415,
    "secondVaccination": {
        "delta": 681084,
        "quote": 0.19621041644895637,
        "vaccinated": 16318175,
        "vaccination": {
        "astraZeneca": 775047,
        "biontech": 13698210,
        "janssen": 662672,
        "moderna": 1182246
        }
    },
    "states": {
        "BB": {
        "administeredVaccinations": 1494757,
        "delta": 18036,
        "indication": {
            "age": null,
            "job": null,
            "medical": null,
            "nursingHome": null,
            "secondVaccination": {
            "age": null,
            "job": null,
            "medical": null,
            "nursingHome": null
            }
        },
        "name": "Brandenburg",
        "quote": 0.3948732162704761,
        "secondVaccination": {
            "delta": 18526,
            "quote": 0.1978390835772969,
            "vaccinated": 498929,
            "vaccination": {
            "astraZeneca": 29373,
            "biontech": 399877,
            "janssen": 20768,
            "moderna": 48911
            }
        },
        "vaccinated": 995828,
        "vaccination": {
            "astraZeneca": 237016,
            "biontech": 681152,
            "moderna": 77660
        }
        },
        ...


----------


The number of vaccinated people are also recorded on a daily basis.
If no days_limit is specified all recorded datapoints are returned by the method::

    data = covid.vaccinations_timeseries(days_limit=6)['data']
    print(data)

Output::

    {
    "history": [
        {
        "date": "2021-05-31T00:00:00.000Z",
        "firstVaccination": 176073,
        "secondVaccination": 355866,
        "vaccinated": 176073
        },
        {
        "date": "2021-06-01T00:00:00.000Z",
        "firstVaccination": 397954,
        "secondVaccination": 563482,
        "vaccinated": 397954
        },
        {
        "date": "2021-06-02T00:00:00.000Z",
        "firstVaccination": 511668,
        "secondVaccination": 681084,
        "vaccinated": 511668
        }
    ]
    }


------------


Testing
-------


The number of people tested for COVID-19 are recorded on a weekly basis.
if no weeks_limit is specified all recorded datapoints are returned by the method::

    data = covid.testing_timeseries(weeks_limit=3)['data']
    print(data)

Output::

    {
    "history": [
        {
        "calendarWeek": "19/2021",
        "laboratoryCount": 210,
        "performedTests": 1100259,
        "positiveTests": 90312,
        "positivityRate": 0.08208249148609555
        },
        {
        "calendarWeek": "20/2021",
        "laboratoryCount": 207,
        "performedTests": 1215641,
        "positiveTests": 70140,
        "positivityRate": 0.05769795523513932
        },
        {
        "calendarWeek": "21/2021",
        "laboratoryCount": 202,
        "performedTests": 936414,
        "positiveTests": 38972,
        "positivityRate": 0.04161834402304963
        }
    ]
    }

"""List of API endpoints `covid19pyclient` knows about."""

BASE_URL = "https://api.corona-zahlen.org/"

API_PATH = {  # API endpoints (full path: https://api.corona-zahlen.org/germany/history/deaths )
    "germany_accumulated":                  "germany",
    "germany_age_groups":                   "germany/age-groups",
    "germany_timeseries_all":               "germany/history/{types}",
    "germany_timeseries_paginated":         "germany/history/{types}/{days}",

    "states_accumulated":                   "states/",
    "states_by_state":                      "states/{state}",
    "states_by_agegroups":                  "states/age-groups",
    "states_by_state_and_agegroups":        "states/{state}/age-groups",

    "districts_accumulated":                "districts",
    "districts_accumulated_by_ags":         "districts/{ags}",
    "districts_timeseries_all":             "districts/history/{types}",
    "districts_timeseries_paginated":       "districts/history/{types}/{days}",
    "districts_timeseries_by_ag":           "districts/{ags}/history/{types}",
    "districts_timeseries_by_ag_paginated": "districts/{ags}/history/{types}/{days}",

    "vaccination_accumulated":              "vaccinations",
    "vaccination_timeseries_all":           "vaccinations/history",
    "vaccination_timeseries_paginated":     "vaccinations/history/{days}",

    "testing_timeseries_all":               "testing/history",
    "testing_timeseries_paginated":         "testing/history/{weeks}",
}

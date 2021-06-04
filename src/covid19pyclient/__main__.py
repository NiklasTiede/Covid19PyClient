"""Python Wrapper of COVID-19 API. RKI Data are about COVID-19 metrics in Germany."""
from datetime import datetime
from typing import Any
from typing import Dict

import requests

from .endpoints import API_PATH
from .endpoints import BASE_URL
from .exceptions import NoValidDistrictError
from .exceptions import NoValidStateError
from .exceptions import NoValidTypeError
from .valid_parameters import AGS
from .valid_parameters import STATES
from .valid_parameters import TYPES


class CovidData:
    """Access REST API of Robert Koch Institute.
    url: https://api.corona-zahlen.org
    """

    def __init__(self) -> None:
        self.session = requests.Session()
        self.url = ''

    def __make_request(self, endpoint: str) -> Dict[str, Any]:
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def germany_total(self) -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Current total amount of cases, deaths, incidence and
        recovery in germany.

        Returns:
            Dict[str, Any]: data about cases, deaths, delta etc.
        """
        self.url = BASE_URL + API_PATH["germany_accumulated"].format()
        return self.__make_request(self.url)

    def germany_timeseries(self, days_limit: int = 0, selected_type: str = 'cases') -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Daily amounts of cases, incidence, deaths and recovered patients
        in germany recorded as timeseries.

        Args:
            days_limit (int, optional): Number of latest datapoints can be limited. Defaults to no limit.
            selected_type (str, optional): Select between 'cases', 'deaths', 'incidence', 'recovered'. Defaults to cases.

        Raises:
            NoValidTypeError: If no valid type ('cases', 'incidence', 'deaths', 'recovered') was chosen.

        Returns:
            Dict[str, Any]: data -> tuples containing the amount of `selected_type` and date
                            meta -> information about lastUpdate and API maintainer
        """
        if selected_type not in TYPES:
            raise NoValidTypeError(selected_type)
        elif days_limit:
            self.url = BASE_URL + API_PATH["germany_timeseries_paginated"].format(types=selected_type, days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["germany_timeseries_all"].format(types=selected_type)
        return self.__make_request(self.url)

    def germany_by_agegroups(self) -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Current total amount of data broken down by age cohorts and gender.

        Returns:
            Dict[str, Any]: data -> metrics about cases and deaths on males/females in different age cohorts
                            meta -> information about lastUpdate and API maintainer
        """
        self.url = BASE_URL + API_PATH["germany_age_groups"]
        return self.__make_request(self.url)

    def states_total(self, state: str = '') -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Current total amount of cases, incidence, deaths and
        recovered patients sorted by geolocation (states).

        Args:
            state (str, optional): A german federal state represented as as 2-letter code. Defaults to all states.

        Raises:
            NoValidStateError: If no valid state was chosen (see valid_parameters.py).

        Returns:
            Dict[str, Any]: data -> metrics about cases and deaths etc. within a specified state
                            meta -> information about lastUpdate and API maintainer
        """
        if state and state not in STATES:
            raise NoValidStateError(state)
        elif state:
            self.url = BASE_URL + API_PATH["states_by_state"].format(state=state)
        else:
            self.url = BASE_URL + API_PATH["states_accumulated"].format(state=state)
        return self.__make_request(self.url)

    def states_by_agegroups(self, state: str = '') -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Current total amount of data per state broken down by age cohorts and gender.

        Args:
            state (str, optional): A german federal state represented as as 2-letter code. Defaults to all states.

        Raises:
            NoValidStateError: If no valid state was chosen (see valid_parameters.py).

        Returns:
            Dict[str, Any]: data -> metrics about total number of cases/deaths on males/females in different age
                                    cohorts within the specified state
                            meta -> information about lastUpdate and API maintainer
        """
        if state and state not in STATES:
            raise NoValidStateError(state)
        elif state and state in STATES:
            self.url = BASE_URL + API_PATH["states_by_state_and_agegroups"].format(state=state)
        else:
            self.url = BASE_URL + API_PATH["states_by_agegroups"].format(state=state)
        return self.__make_request(self.url)

    def districts_total(self, ag: str = '') -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Current total amount of cases, incidence, deaths and
        recovered patients sorted by geolocation (districts).

        Args:
            ag (str, optional): 5-digit community identification number (amtlicher gemeindeschlüssel).
            Defaults to all districts.

        Raises:
            NoValidDistrictError: If no valid district was chosen (see valid_parameters.py).

        Returns:
            Dict[str, Any]: data -> metrics about total cases, deaths etc. within the specified district
                            meta -> information about lastUpdate and API maintainer
        """
        if ag not in AGS:
            raise NoValidDistrictError(ag)
        elif ag:
            self.url = BASE_URL + API_PATH["districts_accumulated_by_ags"].format(ags=ag)
        else:
            self.url = BASE_URL + API_PATH["districts_accumulated"].format()
        return self.__make_request(self.url)

    def districts_timeseries(self, ag: str = '', days_limit: int = 0, selected_type: str = 'cases') -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Daily amounts of cases, incidence, deaths and recovered patients
        per district recorded as timeseries.

        Args:
            ag (str, optional): 5-digit community identification number (amtlicher gemeindeschlüssel). Defaults
            to all districts.
            days_limit (int, optional): Number of latest datapoints can be limited. Defaults to no limit.
            selected_type (str, optional): Select between 'cases'/'deaths'/'incidence'/'recovered'. Defaults to 'cases'.

        Raises:
            NoValidDistrictError: If no valid district was chosen (see valid_parameters.py).
            NoValidTypeError: If no valid type (cases, incidence, deaths, recovered) was chose.

        Returns:
            Dict[str, Any]: data -> datapoints about the amount of the `selected_type` and its date
                            meta -> information about lastUpdate and API maintainer
        """
        ag = str(ag)
        if ag and ag not in AGS:
            raise NoValidDistrictError(ag)
        elif selected_type not in TYPES:
            raise NoValidTypeError(selected_type)
        elif days_limit and ag:
            self.url = BASE_URL + API_PATH["districts_timeseries_by_ag_paginated"].format(types=selected_type, ags=ag, days=days_limit)
        elif ag:
            self.url = BASE_URL + API_PATH["districts_timeseries_by_ag"].format(types=selected_type, ags=ag)
        elif days_limit:
            self.url = BASE_URL + API_PATH["districts_timeseries_paginated"].format(types=selected_type, days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["districts_timeseries_all"].format(types=selected_type)
        return self.__make_request(self.url)

    def vaccinations_total(self) -> Dict[str, Any]:
        """Epidemiological data on COVID-19. The number of vaccination doses administered for the
        country and each state is returned. Vaccinations per supplier is described.

        Returns:
            Dict[str, Any]: data -> data on the total amount vaccinations (country and per state)
                            meta -> information about lastUpdate and API maintainer
        """
        self.url = BASE_URL + API_PATH["vaccination_accumulated"].format()
        return self.__make_request(self.url)

    def vaccinations_timeseries(self, days_limit: int = 0) -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Timeseries data of vaccinations are recorded
        on a daily basis.

        Args:
            days_limit (int, optional): Number of latest datapoints can be limited. Defaults to no limit.

        Returns:
            Dict[str, Any]: data -> datapoints about the amount of vaccinations and its date
                            meta -> information about lastUpdate and API maintainer
        """
        if days_limit:
            self.url = BASE_URL + API_PATH["vaccination_timeseries_paginated"].format(days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["vaccination_timeseries_all"].format()
        return self.__make_request(self.url)

    def testing_timeseries(self, weeks_limit: int = 0) -> Dict[str, Any]:
        """Epidemiological data on COVID-19. Timeseries data of tests are recorded
        on a weekly basis.

        Args:
            weeks_limit (int, optional): Number of latest datapoints can be limited. Defaults to no limit.

        Returns:
            Dict[str, Any]: data -> datapoints about the number of tests and its date
                            meta -> information about lastUpdate and API maintainer
        """
        if weeks_limit:
            self.url = BASE_URL + API_PATH["testing_timeseries_paginated"].format(weeks=weeks_limit)
        else:
            self.url = BASE_URL + API_PATH["testing_timeseries_all"].format()
        return self.__make_request(self.url)


def datereader(date: str) -> datetime:
    """Turns the datetime string retrieved in the API responses into a datetime object (datetime standard module).

    Args:
        date (str): datetime value used within the API.

    Returns:
        [datetime.datetime]: datetime object
    """
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

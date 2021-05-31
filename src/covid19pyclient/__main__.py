"""Python Wrapper of COVID-19 API. RKI Data are about COVID-19 metrics in Germany."""
from typing import Any
from typing import Dict

import requests

from .endpoints import API_PATH
from .endpoints import BASE_URL
from .endpoints import STATES
from .endpoints import TYPES
from .exceptions import NoValidStateError
from .exceptions import NoValidTypeError


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
        """Accumulated numbers of SARS-CoV-2-related cases, deaths and recovery at this point of time in germany.

        Returns:
            Dict[str, Any]: cases, casesPer100k, casesPerWeek, deaths, delta, r, recovered, weekIncidence, meta.
        """
        self.url = BASE_URL + API_PATH["germany_accumulated"].format()
        return self.__make_request(self.url)

    def germany_timeseries(self, days_limit: int = 0, selected_type: str = 'cases') -> Dict[str, Any]:
        """The daily numbers of cases, incidence, deaths and recovered patients in germany are recorded as timeseries.

        Args:
            days_limit (int, optional): number of latest datapoints can be limited. Defaults to no limit.
            selected_type (str, optional): select between cases/deaths/incidence and x. Defaults to 'cases'.

        Raises:
            NoValidTypeError: if no valid `selected_type`-arg (cases, incidence, deaths, recovered) was provided.

        Returns:
            Dict[str, Any]: data -> tuples of the amount of `selected_type` and date
                            meta ->
        """
        if selected_type not in TYPES:
            raise NoValidTypeError(selected_type)
        elif days_limit:
            self.url = BASE_URL + API_PATH["germany_timeseries_paginated"].format(types=selected_type, days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["germany_timeseries_all"].format(types=selected_type)
        return self.__make_request(self.url)

    def germany_by_agegroups(self) -> Dict[str, Any]:
        """data about all persons sorted by age groups.

        Returns:
            Dict[str, Any]: returns accumulated data as dict
        """
        self.url = BASE_URL + API_PATH["germany_age_groups"]
        return self.__make_request(self.url)

    def states_total(self, selected_state: str = '') -> Dict[str, Any]:
        """data accumulated according sorted by geolocation (states)

        Args:
            selected_state (str, optional): one of 16 germany state as 2-letter code. Defaults to ''.

        Raises:
            NoValidStateError: if not chosen a selected type correctly

        Returns:
            Dict[str, Any]: dict of data
        """
        if selected_state and selected_state not in STATES:
            raise NoValidStateError(selected_state)
        elif selected_state:
            self.url = BASE_URL + API_PATH["states_by_state"].format(state=selected_state)
        else:
            self.url = BASE_URL + API_PATH["states_accumulated"].format(state=selected_state)
        return self.__make_request(self.url)

    def states_by_agegroups(self, selected_state: str = '') -> Dict[str, Any]:
        """[summary]

        Args:
            selected_state (str, optional): [description]. Defaults to ''.

        Raises:
            NoValidStateError: [description]

        Returns:
            Dict[str, Any]: [description]
        """
        if selected_state and selected_state not in STATES:
            raise NoValidStateError(selected_state)
        elif selected_state and selected_state in STATES:
            self.url = BASE_URL + API_PATH["states_by_state_and_agegroups"].format(state=selected_state)
        else:
            self.url = BASE_URL + API_PATH["states_by_agegroups"].format(state=selected_state)
        return self.__make_request(self.url)

    def districts_total(self) -> Dict[str, Any]:
        """[summary]

        Returns:
            Dict[str, Any]: [description]
        """
        self.url = BASE_URL + API_PATH["districts_accumulated"].format()
        return self.__make_request(self.url)

    def districts_timeseries(self, days_limit: int = 0, selected_type: str = 'cases') -> Dict[str, Any]:
        """[summary]

        Args:
            days_limit (int, optional): [description]. Defaults to 0.
            selected_type (str, optional): [description]. Defaults to 'cases'.

        Raises:
            NoValidTypeError: [description]

        Returns:
            Dict[str, Any]: [description]
        """
        if selected_type not in TYPES:
            raise NoValidTypeError(selected_type)
        elif days_limit:
            self.url = BASE_URL + API_PATH["districts_timeseries_paginated"].format(types=selected_type, days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["districts_timeseries_all"].format(types=selected_type)
        return self.__make_request(self.url)

    def vaccinations_total(self) -> Dict[str, Any]:
        """[summary]

        Returns:
            Dict[str, Any]: [description]
        """
        self.url = BASE_URL + API_PATH["vaccination_accumulated"].format()
        return self.__make_request(self.url)

    def vaccinations_timeseries(self, days_limit: int = 0) -> Dict[str, Any]:
        """[summary]

        Args:
            days_limit (int, optional): [description]. Defaults to 0.

        Returns:
            Dict[str, Any]: [description]
        """
        if days_limit:
            self.url = BASE_URL + API_PATH["vaccination_timeseries_paginated"].format(days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["vaccination_timeseries_all"].format()
        return self.__make_request(self.url)

    def testing_timeseries(self, weeks_limit: int = 0) -> Dict[str, Any]:
        """[summary]

        Args:
            weeks_limit (int, optional): [description]. Defaults to 0.

        Returns:
            Dict[str, Any]: [description]
        """
        if weeks_limit:
            self.url = BASE_URL + API_PATH["testing_timeseries_paginated"].format(weeks=weeks_limit)
        else:
            self.url = BASE_URL + API_PATH["testing_timeseries_all"].format()
        return self.__make_request(self.url)

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

    def germany_timeseries(self, days_limit: int = 0, sel_type: str = 'cases') -> Dict[str, Any]:
        if sel_type not in TYPES:
            raise NoValidTypeError(sel_type)
        elif days_limit:
            self.url = BASE_URL + API_PATH["germany_history_paginated"].format(types=sel_type, days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["germany_history"].format(types=sel_type)
        return self.__make_request(self.url)

    def germany_total(self) -> Dict[str, Any]:
        self.url = BASE_URL + API_PATH["germany_accumulated"].format()
        return self.__make_request(self.url)

    def germany_by_agegroups(self) -> Dict[str, Any]:
        self.url = BASE_URL + API_PATH["germany_age_groups"]
        return self.__make_request(self.url)

    def by_states(self, selected_state: str = '') -> Dict[str, Any]:
        if selected_state and selected_state not in STATES:
            raise NoValidStateError(selected_state)
        elif selected_state:
            self.url = BASE_URL + API_PATH["states_history"].format(state=selected_state)
        else:
            self.url = BASE_URL + API_PATH["states_accumulated"].format(state=selected_state)
        return self.__make_request(self.url)

    def by_states_by_agegroups(self, selected_state: str = '') -> Dict[str, Any]:
        if selected_state and selected_state not in STATES:
            raise NoValidStateError(selected_state)
        elif selected_state and selected_state in STATES:
            self.url = BASE_URL + API_PATH["states_all_by_agegroups"].format(state=selected_state)
        else:
            self.url = BASE_URL + API_PATH["states_by_agegroups"].format(state=selected_state)
        return self.__make_request(self.url)

    def districts_total(self) -> Dict[str, Any]:
        self.url = BASE_URL + API_PATH["districts_accumulated"].format()
        return self.__make_request(self.url)

    def districts_timeseries(self, days_limit: int = 0, sel_type: str = 'cases') -> Dict[str, Any]:
        if sel_type not in TYPES:
            raise NoValidTypeError(sel_type)
        elif days_limit:
            self.url = BASE_URL + API_PATH["districts_history_paginated"].format(types=sel_type, days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["districts_history"].format(types=sel_type)
        return self.__make_request(self.url)

    def vaccinations_total(self) -> Dict[str, Any]:
        self.url = BASE_URL + API_PATH["vaccination_accumulated"].format()
        return self.__make_request(self.url)

    def vaccinations_timeseries(self, days_limit: int = 0) -> Dict[str, Any]:
        if days_limit:
            self.url = BASE_URL + API_PATH["vaccination_history_paginated"].format(days=days_limit)
        else:
            self.url = BASE_URL + API_PATH["vaccination_history"].format()
        return self.__make_request(self.url)

    def testing_timeseries(self, weeks_limit: int = 0) -> Dict[str, Any]:
        if weeks_limit:
            self.url = BASE_URL + API_PATH["testing_history_paginated"].format(weeks=weeks_limit)
        else:
            self.url = BASE_URL + API_PATH["testing_history"].format()
        return self.__make_request(self.url)

"""Main module."""

from pprint import pprint

import requests

# https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python


api_url = 'https://api.corona-zahlen.org/germany'

# payload = {"countryRegion": "United Kingdom"}
payload = {}

resp = requests.get(
    api_url,
    # params=payload,
    )

pprint(len(resp.json()))

data = resp.json()
pprint(data)


print(type(data['cases']), data['cases'])



from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Germany(BaseModel):
    cases: int
    deaths: int
    recovered: int
    weekIncidence: float
    casesPer100k: float
    casesPerWeek: float


    y: Optional[datetime] = None
    x: List[int] = []


germany = Germany(**resp.json())

print(germany.weekIncidence)
print(germany.deaths)


# create for each endpoint the classes, but how to create classes so others can use it?


class GermanyData:
    def __init__(self) -> None:
        # germany = Germany(**resp.json())
        self.data = Germany(**resp.json())

    @staticmethod
    def get_cases() -> int:
        return data['cases']



cases2 = GermanyData.get_cases()
print(type(cases2), cases2)



# https://github.com/SaidBySolo/SpaceXPy
# https://api.spacexdata.com/v4/launches/latest

# https://github.com/bear/python-twitter/blob/master/twitter/api.py
# https://github.com/PyGithub/PyGithub
#








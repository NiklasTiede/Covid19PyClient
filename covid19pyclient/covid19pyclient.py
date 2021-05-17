"""Main module."""

import requests
from pprint import pprint

api_url = 'https://covid19.mathdro.id/api'

resp = requests.get(api_url)


pprint(resp.text)


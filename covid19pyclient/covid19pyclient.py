"""Main module."""
from pprint import pprint

import requests

api_url = 'https://covid19.mathdro.id/api'

resp = requests.get(api_url)


pprint(resp.text)

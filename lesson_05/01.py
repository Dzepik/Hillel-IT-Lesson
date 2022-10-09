"""
вивести список всіх астронавтів, що перебувають в даний момент на орбіті
(дані не фейкові, оновлюються в режимі реального часу)
"""
import requests
from pprint import pprint
import json
url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
response_dict = json.loads(response.content)
people = response_dict['people']
astronavt_name = []

for craft in people:
    astronavt_name.append(craft['name'])
pprint(astronavt_name)
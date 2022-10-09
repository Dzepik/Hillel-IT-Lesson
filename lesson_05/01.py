"""
вивести список всіх астронавтів, що перебувають в даний момент на орбіті
(дані не фейкові, оновлюються в режимі реального часу)
"""
import requests
from pprint import pprint

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url).json()

people = response['people']
astronavt_name = []

for craft in people:
    astronavt_name.append(craft['name'])
pprint(astronavt_name)
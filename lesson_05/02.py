"""
апі погоди
"""

import requests
from pprint import pprint

url = 'https://api.openweathermap.org/data/2.5/weather?q=dnipro&appid=47503e85fabbabc93cff28c52398ae97&units=metric '

response = requests.get(url).json()
pprint(response)
name_city = response['name']
speed_wind = response['wind']['speed']
temperature = response['main']['temp']

print(f'{name_city} speed wind {speed_wind} m/sec, temperature of air {temperature}')


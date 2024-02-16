#
#
#

import requests
import json
# code for temperature
url = "https://api.open-meteo.com/v1/forecast?latitude=52.6446122&longitude=-9.481083&current=temperature_2m"
response = requests.get(url) 
data = response.json()
current_units = data["current"]
temperature = current_units["temperature_2m"]
print (f' The temperature is: {temperature} degrees C')


 # code for wind speed
url = "https://api.open-meteo.com/v1/forecast?latitude=52.6446122&longitude=-9.481083&current=wind_speed_10m"
response = requests.get(url) 
data = response.json()
current_units = data["current"]
windspeed = current_units["wind_speed_10m"]
print (f' The wind speed is: {windspeed} km/h')

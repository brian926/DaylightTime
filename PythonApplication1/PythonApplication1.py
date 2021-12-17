import requests
from datetime import datetime
import pytz

url = "https://api.sunrise-sunset.org/json?lat=41&lng=-71&date=today&formatted=0"
response = requests.get(url)
data = response.json()

def get_sunrise(response):
    sunrise = response['results']['sunrise']
    return sunrise

def get_sunset(response):
    sunset = response['results']['sunset']
    sunset_est = convert_utc(sunset)
    return sunset_est

def convert_utc(utc_time):
    new_time = datetime.fromisoformat(utc_time)

    fmt = '%Y-%m-%dT%H:%M:%S %Z%z'

    print(new_time.strfttime(fmt))

    return new_time.astimezone(est).strftime(fmt)

print(get_sunset(data))
import requests
from datetime import datetime
import pytz

def get_data(lat = 41, log = -71):
    url = "https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today&formatted=0".format(lat, log)
    response = requests.get(url)
    data = response.json()
    return data

def convert_utc(utc_time):
    new_time = datetime.fromisoformat(utc_time)

    fmt = '%H:%M:%S %Z'
    est = pytz.timezone("US/Eastern")
    print(new_time.strftime(fmt))

    return new_time.astimezone(est).strftime(fmt)

def get_sunrise(response):
    sunrise = response['results']['sunrise']
    sunrise_est = convert_utc(sunrise)
    return sunrise_est

def get_sunset(response):
    sunset = response['results']['sunset']
    sunset_est = convert_utc(sunset)
    return sunset_est


test = get_data()
print(test['results'])
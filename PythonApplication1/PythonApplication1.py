import requests
from datetime import datetime
import pytz
import schedule
from geopy.geocoders import Nominatim


def get_data(lat = 41, log = -71):
    url = "https://api.sunrise-sunset.org/json?lat={}&lng={}&date=today&formatted=0".format(lat, log)
    response = requests.get(url)
    data = response.json()
    return data

def get_coord(city_name):
    gn = Nominatim(user_agent='myapplication')
    result = gn.geocode(city_name)
    return result.raw

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

def check_time(est_time):
    est_time = est_time.strftime('%H:%M:%S')

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')

    if est_time > current_time:
        return -1
    elif est_time < current_time:
        return 1
    else:
        return 0

def test_run(sr_time, ss_time):
    while True:
        sunrise = check_time(sr_time)
        sunset = check_time(ss_time)

        if sunrise == 0:
            print("Sunrise is now")
        elif sunrise == 1 and sunset < 1:
            print("Sun has rised sunset is at {}".format(sunset))
        elif sunrise < 1:
            print("Sun has set")

def pull_data():
    schedule.every().day.at("02:30").do(run_jobs)

def run_jobs():
    info = get_data()
    sunset = get_sunset(info)
    sunrise = get_sunrise(info)
    test_run(sunrise, sunset)


def test_run():
    test = get_coord("New haven, CT")
    lat = test['lat']
    log = test['lon']
    data = get_data(lat, log)
    sunrise = get_sunrise(data)
    sunset = get_sunset(data)
    test_run(sunrise, sunset)


test_run()
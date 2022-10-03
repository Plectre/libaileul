
import requests
import json
from time import time, ctime

## https://api.openweathermap.org


def get_weather():
    is_connected = False

    data =      {    
                'appid':'10c5bcd01a088e1338f12e51b7aaeb39',
                'lang':'fr',
                'units':'metric',
                'coord': {"lat":44.70208,
                        "lon":-0.77969},
                }

    url = f'https://api.openweathermap.org/data/2.5/weather?lang={data["lang"]}&units={data["units"]}&lat={data["coord"]["lat"]}&lon={data["coord"]["lon"]}&appid={data["appid"]}'

    try:
        weather_data = requests.get(url)
        print('connected !')
        is_connected = True
    except:
        print('not connected !')
        with open('./weather.json') as read_file:
            w = json.load(read_file)
            result = format_result(w)

    if is_connected:
        if weather_data.status_code == 200:
            w = json.loads(weather_data.content)
            result = format_result(w)
            return result
        else:
            return result



def convert_time(t):
    c = ctime(t)
    ## ctime return a tuple
    return c[-13:-8]


def format_result(w):
    sunrise = convert_time(w['sys']['sunrise'])
    sunset = convert_time(w['sys']['sunset'])
    dt = convert_time(w['dt'])
    dt = "{0}h{1}".format(dt[0:2], dt[3:5])

    result = {
                'heure': str(dt),
                'temperature': w['main']['temp'],
                'pression': w['main']['pressure'],
                'wind_speed': w['wind']['speed'],
                'wind_direction': w['wind']['deg'],
                'clouds': w['clouds']['all'],
                'sunrise': str(sunrise),
                'sunset': str(sunset),
            }
    return result

def sort_time():
    print("sort_time")

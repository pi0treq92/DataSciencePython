import numpy as np
import pandas as pd
import datetime
import json
import requests
import time
gdansk ={}
torun = {}
wloclawek = {}
poznan = {}
szczecin = {}
warszawa = {}
tczew = {}
krakow = {}
katowice = {}
rzeszow = {}

def prepare(city,city_name):
    temp = [ ]
    humidity = [ ]
    pressure = [ ]
    description = [ ]
    dt = [ ]
    wind_speed = [ ]
    temp.append(city['main']['temp']-273.15)
    humidity.append(city['main']['humidity'])
    pressure.append(city['main']['pressure'])
    description.append(city['weather'][0]['description'])
    dt.append(city['dt'])
    wind_speed.append(city['wind']['speed'])
    headings = ['temp','humidity','pressure','description','dt','wind_speed']
    data = [temp, humidity, pressure, description, dt, wind_speed]
    df = pd.DataFrame(data, index=headings)
    city = df.T
    city['city'] = city_name
    city['day'] = city['dt'].apply(datetime.datetime.fromtimestamp)
    return city

df_gdansk = []
df_torun = []
df_katowice = []
df_wloclawek = []
df_warszawa = []
df_rzeszow = []
df_krakow = []
df_tczew = []
df_poznan = []
df_szczecin = []

df_tables = [df_gdansk, df_torun, df_katowice, df_wloclawek, df_warszawa, df_rzeszow, df_krakow, df_tczew, df_poznan,df_szczecin]
city_table = [gdansk, torun, katowice, wloclawek, warszawa, rzeszow, krakow, tczew, poznan, szczecin]
city_names = [str(i) for i in city_table]

for i in range(28):
    gdansk['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                     'weather?q=Gdansk,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    torun['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                    'weather?q=torun,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    wloclawek['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                        'weather?q=wloclawek,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    poznan['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                     'weather?q=poznan,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    szczecin['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                       'weather?q=szczecin,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    warszawa['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                       'weather?q=warszawa,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    tczew['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                    'weather?q=tczew,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    krakow['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                     'weather?q=krakow,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    katowice['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                       'weather?q=katowice,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    rzeszow['{}'.format(i)] = json.loads(requests.get('http://api.openweathermap.org/data/2.5/'
                                      'weather?q=rzeszow,PL&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
    time.sleep(900)

for j in range(len(city_table)):
    with open(str('{}'.format(city_table[j]['0']['name'])+'.json').lower(), mode='w') as f:
        json.dump(city_table[j], f, indent=4)




#df_gdansk=pd.read_json('gdansk.json')


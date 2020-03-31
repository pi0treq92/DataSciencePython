import numpy as np
import pandas as pd
import datetime
import json
import requests
import time

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


df_gdansk=pd.read_json('Gdańsk.json')
df_katowice=pd.read_json('Katowice.json')
df_krakow=pd.read_json('Krakow.json')
df_poznan=pd.read_json('Poznań.json')
df_rzeszow=pd.read_json('Rzeszów.json')
df_szczecin=pd.read_json('Szczecin.json')
df_tczew=pd.read_json('Tczew.json')
df_torun=pd.read_json('Toruń.json')
df_warszawa=pd.read_json('Warsaw.json')
df_wloclawek=pd.read_json('Włocławek.json')
gdansk_prepared=prepare(df_gdansk[0], 'Gdańsk')
kato_prepared=prepare(df_katowice[0], 'Katowice')
krk_prepared=prepare(df_krakow[0], 'Kraków')
poz_prepared=prepare(df_poznan[0], 'Poznań')
rze_prepared=prepare(df_rzeszow[0], 'Rzeszów')
szc_prepared=prepare(df_szczecin[0], 'Szczecin')
tcz_prepared=prepare(df_tczew[0], 'Tczew')
tor_prepared=prepare(df_torun[0], 'Toruń')
war_prepared=prepare(df_warszawa[0], 'Warszawa')
wlo_prepared=prepare(df_wloclawek[0], 'Włocławek')
df_cities = [df_gdansk, df_katowice, df_krakow, df_poznan, df_rzeszow, df_szczecin, df_tczew, df_torun, df_warszawa, df_wloclawek]
city_prepared = [gdansk_prepared,kato_prepared,krk_prepared,poz_prepared,rze_prepared,szc_prepared,tcz_prepared,tor_prepared,war_prepared,wlo_prepared]
for i in range(len(city_prepared)):
    for j in range(1, 28):
        city_prepared[i] = city_prepared[i].append(prepare(df_cities[i][j], '{}'.format(df_cities[i][0]['name'])), ignore_index=True)

city_prepared[0]['dist'] = 0
city_prepared[1]['dist'] = 457
city_prepared[2]['dist'] = 483
city_prepared[3]['dist'] = 215
city_prepared[4]['dist'] = 515
city_prepared[5]['dist'] = 56
city_prepared[6]['dist'] = 30
city_prepared[7]['dist'] = 150
city_prepared[8]['dist'] = 266
city_prepared[9]['dist'] = 190
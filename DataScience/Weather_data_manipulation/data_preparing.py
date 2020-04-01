import numpy as np
import pandas as pd
import datetime
import json
import requests
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
def prepare(city,city_name):
    temp = [ ]
    humidity = [ ]
    pressure = [ ]
    description = [ ]
    dt = [ ]
    wind_deg = []
    wind_speed = [ ]
    temp.append(city['main']['temp']-273.15)
    humidity.append(city['main']['humidity'])
    pressure.append(city['main']['pressure'])
    description.append(city['weather'][0]['description'])
    dt.append(city['dt'])
    wind_speed.append(city['wind']['speed'])
    try:
        wind_deg.append(city['wind']['deg'])
    except:
        wind_deg.append(0)
    headings = ['temp','humidity','pressure','description','dt','wind_speed', 'wind_deg']
    data = [temp, humidity, pressure, description, dt, wind_speed, wind_deg]
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


def tempTrendChart(*args):
    x = [[] for i in range(len(args))]
    y = [[] for j in range(len(args))]
    for counter, arg in enumerate(args):
        x[counter] = arg['day']
        y[counter] = arg['temp']
    plt.xticks(rotation=70)
    plt.title('Daily temperature chart')
    plt.plot(x[0], y[0], 'r', x[1], y[1], 'b', x[2], y[2], 'k')
    if len(x)>3:
        try:
            plt.plot(x[3], y[3], 'g', x[4], y[4], 'y')
        except:
            pass
    plt.legend([arg['city'][0] for arg in args], loc=4)
    plt.show()

def humTrendChart(*args):
    x = [[] for i in range(len(args))]
    y = [[] for j in range(len(args))]
    for counter, arg in enumerate(args):
        x[counter] = arg['day']
        y[counter] = arg['humidity']
    plt.xticks(rotation=70)
    plt.title('Daily humidity chart')
    plt.plot(x[0], y[0], 'r', x[1], y[1], 'b', x[2], y[2], 'k')
    if len(x)>3:
        try:
            plt.plot(x[3], y[3], 'g', x[4], y[4], 'y')
        except:
            pass
    plt.legend([arg['city'][0] for arg in args], loc=4)
    plt.show()

def distanceHumidityCorrelation(cities):
    dist = [city['dist'][0] for city in cities]
    hum_max = [city['humidity'].max() for city in cities]
    hum_min = [city['humidity'].min() for city in cities]
    return dist, hum_max, hum_min

def distanceTempCorrelation(cities):
    dist = [city['dist'][0] for city in cities]
    temp_max = [city['temp'].max() for city in cities]
    temp_min = [city['temp'].min() for city in cities]
    return dist, temp_max, temp_min

def linearRegression(dist, dat_max, dat_min):
    x = np.array(dist)
    y = np.array(dat_max)
    z = np.array(dat_min)
    x1 = x[x < 100]
    x1 = x1.reshape((x1.size, 1))
    y1 = y[x < 100]
    z1 = z[x < 100]
    x2 = x[x > 100]
    x2 = x2.reshape((x2.size, 1))
    y2 = y[x > 100]
    z2 = z[x > 100]
    from sklearn.svm import SVR
    svr_lin1 = SVR(kernel='linear', C=1e3)
    svr_lin2 = SVR(kernel='linear', C=1e3)
    svr_lin3 = SVR(kernel='linear', C=1e3)
    svr_lin4 = SVR(kernel='linear', C=1e3)
    svr_lin1.fit(x1, y1)
    svr_lin2.fit(x2, y2)
    svr_lin3.fit(x1, z1)
    svr_lin4.fit(x2, z2)
    xp1 = np.arange(0, 90, 10).reshape((9, 1))
    xp2 = np.arange(100, 590, 70).reshape((7, 1))
    yp1 = svr_lin1.predict(xp1)
    yp2 = svr_lin2.predict(xp2)
    zp1 = svr_lin3.predict(xp1)
    zp2 = svr_lin4.predict(xp2)
    plt.plot(xp1, yp1, c='r', label='Strong sea effect of max data')
    plt.plot(xp2, yp2, c='b', label='Light sea effect of max data')
    plt.plot(xp1, zp1, c='g', label='Strong sea effect of min data')
    plt.plot(xp2, zp2, c='y', label='Light sea effect of min data')
    if max(dat_max) <7:
        plt.axis((-5, 500, 0, 7))
        plt.title('Linear regression for temp-distance relation')
        plt.legend(['Max data up to 100 km', 'Max data over 100 km', 'Min data up to 100 km', 'Max data over 100 km'],
                   loc=7)
    elif max(dat_max) >7 and max(dat_max) <15:
        plt.axis((-5, 500, 0, 15))
        plt.title('Linear regression for wind-distance relation')
        plt.legend(['Max data up to 100 km', 'Max data over 100 km', 'Min data up to 100 km', 'Max data over 100 km'],
                   loc=7)
    else:
        plt.axis((-5, 500, 10, 100))
        plt.title('Linear regression for humidity-distance relation')
        plt.legend(['Max data up to 100 km', 'Max data over 100 km', 'Min data up to 100 km', 'Max data over 100 km'],
                   loc=4)

    plt.scatter(x, y, c='r', label='data')
    plt.scatter(x, z, c='b', label='data')
    plt.xlabel('Distance [km]', color='gray')
    plt.ylabel('Data', color='gray')
    plt.show()

def showRoseWind(city):
    hist, bins = np.histogram(city['wind_deg'], 8, [0, 360])
    max_value = max(hist)
    N=8
    theta = np.arange(0.,2*np.pi, 2*np.pi/N)
    radian = np.array(hist)
    plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
    colors = [(1-x/max_value, 1-x/max_value, 0.75) for x in radian]
    plt.bar(theta +np.pi/8, radian, width=(2*np.pi/N), bottom=0.0, color=colors)
    plt.title(city['city'][0], x=0.2, fontsize=20)
    plt.show()

def showRoseWindVelocity(city):
    degs = np.arange(45,361,45)
    tmp = []
    for deg in degs:
        tmp.append(city[(city['wind_deg']>(deg-46)) & (city['wind_deg']<deg)]['wind_speed'].mean())
    velocity = np.nan_to_num(tmp)
    theta = np.arange(0., 2 * np.pi, 2 * np.pi / 8)
    radian = np.array(velocity)
    plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
    colors = [(1 - x /10, 1 - x / 10, 0.75) for x in radian]
    plt.bar(theta+np.pi/8, radian, width=(2*np.pi/8), bottom=0.0, color=colors)
    plt.title(city['city'][0])
    plt.show()

showRoseWind(city_prepared[0])
showRoseWindVelocity(city_prepared[0])
tempTrendChart(city_prepared[0], city_prepared[2], city_prepared[4], city_prepared[6],city_prepared[9])
dist, hum_max, hum_min = distanceHumidityCorrelation(city_prepared)
linearRegression(dist, hum_max, hum_min)
dist, temp_max, temp_min = distanceTempCorrelation(city_prepared)
linearRegression(dist, temp_max, temp_min)

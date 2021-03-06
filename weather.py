import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from sklearn.svm import SVR

df_ferrara = pd.read_csv('WeatherData/ferrara_270615.csv')
df_milano = pd.read_csv('WeatherData/milano_270615.csv')
df_mantova = pd.read_csv('WeatherData/mantova_270615.csv')
df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
df_asti = pd.read_csv('WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('WeatherData/bologna_270615.csv')
df_piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
df_cesena = pd.read_csv('WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('WeatherData/faenza_270615.csv')
df_torino = pd.read_csv('WeatherData/torino_270615.csv')
df_list = [df_ravenna, df_cesena, df_faenza, df_ferrara, df_bologna, df_mantova, df_piacenza, df_milano, df_asti]


def Time_temp():
    y1 = df_ravenna['temp']
    x1 = df_ravenna['day']
    y2 = df_faenza['temp']
    x2 = df_faenza['day']
    y3 = df_cesena['temp']
    x3 = df_cesena['day']
    y4 = df_milano['temp']
    x4 = df_milano['day']
    y5 = df_asti['temp']
    x5 = df_asti['day']
    y6 = df_torino['temp']
    x6 = df_torino['day']

    day_ravenna = [parser.parse(x) for x in x1]
    day_faenza = [parser.parse(x) for x in x2]
    day_cesena = [parser.parse(x) for x in x3]
    day_milano = [parser.parse(x) for x in x4]
    day_asti = [parser.parse(x) for x in x5]
    day_torino = [parser.parse(x) for x in x6]

    fig, ax = plt.subplots()
    plt.xticks(rotation=70)

    hours = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(hours)

    ax.plot(day_ravenna, y1, 'r', day_faenza, y2, 'r', day_cesena, y3, 'r')
    ax.plot(day_milano, y4, 'g', day_asti, y5, 'g', day_torino, y6, 'g')
    ax.legend(['cities close to ocean',
                'cities far from the sea'], loc="best")

    plt.xlabel("Time")
    plt.ylabel("Temp")
    plt.show()

def distance_hum():

    y1 = df_ravenna['humidity']
    x1 = df_ravenna['day']
    y2 = df_faenza['humidity']
    x2 = df_faenza['day']
    y3 = df_cesena['humidity']
    x3 = df_cesena['day']
    y4 = df_milano['humidity']
    x4 = df_milano['day']
    y5 = df_asti['humidity']
    x5 = df_asti['day']
    y6 = df_torino['humidity']
    x6 = df_torino['day']

    fig, ax = plt.subplots()
    plt.xticks(rotation=70)

    day_ravenna = [parser.parse(x) for x in x1]
    day_faenza = [parser.parse(x) for x in x2]
    day_cesena = [parser.parse(x) for x in x3]
    day_milano = [parser.parse(x) for x in x4]
    day_asti = [parser.parse(x) for x in x5]
    day_torino = [parser.parse(x) for x in x6]

    hours = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(hours)

    ax.plot(day_ravenna, y1, 'r', day_faenza, y2, 'r', day_cesena, y3, 'r')
    ax.plot(day_milano, y4, 'g', day_asti, y5, 'g', day_torino, y6, 'g')
    plt.xlabel("Time")
    plt.ylabel("humidity")
    plt.title("Humidity v.s. Time")
    plt.show()



def distance_temp():
    dist = []
    temp_max= []
    temp_min = []
    for df in df_list :
        dist.append(df['dist'][0])
        temp_max.append(df['temp'].max())
        temp_min.append(df['temp'].min())

    plt.subplot(1,2,1)
    plt.plot(dist,temp_max,'r--')
    plt.plot(dist,temp_min,'b--')
    plt.legend(['Max Temp', 'Min Temp'], loc="best")
    plt.xlabel("Distance to the ocean")
    plt.ylabel("Temp")

    dist1 = dist[0:4]
    dist2 = dist[5:9]

    dist1 = [[x] for x in dist1]
    dist2 = [[x] for x in dist2]

    temp_max1 = temp_max[0:4]
    temp_max2 = temp_max[5:9]

    svr_lin1 = SVR(kernel='linear', C=1e3)
    svr_lin2 = SVR(kernel='linear', C=1e3)

    svr_lin1.fit(dist1, temp_max1)
    svr_lin2.fit(dist2, temp_max2)

    xp1 = np.arange(10,100,10).reshape((9,1))
    xp2 = np.arange(50,400,50).reshape((7,1))
    yp1 = svr_lin1.predict(xp1)
    yp2 = svr_lin2.predict(xp2)

    plt.subplot(1,2,2)
    plt.plot(xp1, yp1, c='b', label='Strong sea effect')
    plt.plot(xp2, yp2, c='g', label='Light sea effect')
    plt.xlabel("Distance to the ocean")
    plt.ylabel("Temp")
    plt.plot(dist,temp_max,'r--')
    plt.show()


def showRoseWind(values, city_name, max_value):
    N = 8

    # theta = [pi*1/4, pi*2/4, pi*3/4, ..., pi*2]
    theta = np.arange(2 * np.pi / 16, 2 * np.pi, 2 * np.pi / 8)
    radii = np.array(values)

    plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
    colors = [(1-x/max_value, 1-x/max_value, 0.75) for x in radii]
    plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)

    # 设置极区图的标题
    plt.title(city_name, x=0.2, fontsize=20)
    plt.show()


def RoseWind_Speed(df_city):
    # degs = [45, 90, ..., 360]
    degs = np.arange(45, 361, 45)
    tmp = []
    for deg in degs:

        tmp.append(df_city[(df_city['wind_deg'] > (deg-46)) & (df_city['wind_deg'] < deg)]
                   ['wind_speed'].mean())
    return np.array(tmp)


distance_hum()

'''
Time_temp()
distance_temp()
distance_hum()
hist, bins = np.histogram(df_ravenna['wind_deg'], 8, [0, 360])
showRoseWind(hist, 'Ravenna', max(hist))
showRoseWind(RoseWind_Speed(df_ravenna), 'Ravenna', max(hist))
'''

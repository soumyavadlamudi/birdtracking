#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:53:37 2020

@author: roott
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

birddata = pd.read_csv('bird_tracking.csv')
print(birddata.head(5))
birddata.info()

plt.figure(figsize=(7,7))
birdnames = birddata.bird_name.unique()
for bird in birdnames:
    ix = birddata.bird_name == bird

    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y, '.', label = bird)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc = 'lower right')
    

ix = birddata.bird_name == 'Eric'

speed = birddata.speed_2d[ix]
np.sum(np.isnan(speed))
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0,30, 10), normed=False)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")


timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S' ))
    
    
birddata['timestamps'] = pd.Series(timestamps, index = birddata.index)
times = birddata.timestamps[birddata.bird_name == 'Eric']
elapsedtime = [time - times[0] for time in times] 
# to know how many days have passed
elapsedtime[1000]/datetime.timedelta(days = 1)
# to know how many hours have passed
elapsedtime[1000]/datetime.timedelta(hours = 1)
# to know how many hours have passed
elapsedtime[1000]/datetime.timedelta(minutes = 1)
plt.plot(np.array(elapsedtime)/datetime.timedelta(days = 1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time(days)")

data = birddata[birddata.bird_name == 'Eric']
times = data.timestamps
elapsedtime = [time - times[0] for time in times] 
elapsed_days = np.array(elapsedtime)/datetime.timedelta(days = 1)
next_day = 1
daily_mean_speed = []
inds = []
for (i, t) in enumerate(elapsed_days):
    if (t < next_day):
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []
plt.figure(figsize=(7,7))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean spees (m/s)")
    
    




  
  

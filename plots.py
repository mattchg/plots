# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:39:50 2019

@author: Matthew
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import nltk as nl
from scipy import stats

data = pd.read_csv('allen.csv')
data.columns
data = data[['MP','FG','FGA', '3P', '3PA','FT', 'FTA','PTS','AST']].dropna()


#Histogram of Points Scored

plt.figure()
plt.hist(data.PTS,bins=20, density = True) # Density returns a pdf based on the data/bin size
plt.title('Ray Allen: Point Distribution',
          fontsize = 20,
          color='y',
          loc='center')
plt.xlabel("Points Scored",fontsize = 15,color='b')
plt.ylabel("Normalized Frequency",fontsize = 15,color='r')

#Bar of Shooting Percentages
shooting = {}
shooting['Field'] = 100*data['FG'].sum()/data['FGA'].sum()
shooting['Free'] = 100*data['FT'].sum()/data['FTA'].sum()
shooting['Three']= 100*data['3P'].sum()/data['3PA'].sum()

labels = ['Field Goals','Free Throws','Three Pointers']

plt.figure()
plt.bar(x= labels,height = list(shooting.values()),width = 0.5, color = 'b')
plt.title('Ray Allen: Shooting Percentage',
          fontsize = 20,
          color='y',
          loc='center')
plt.xlabel("Type of Shot",fontsize = 15,color='b')
plt.ylabel("Shooting %",fontsize = 15,color='r')
plt.grid(axis='both',color='g', linestyle='-', linewidth=0.5)
plt.show()


#Pie chart of point source (FG,3P,FT)

points = {}
points['Three'] = 3*data['3P'].sum()
points['FG'] = 2*(data['FG'].sum()-data['3P'].sum())
points['Free'] =  data['FT'].sum()
text = {'fontsize': 12}

plt.figure()
plt.pie(x = list(points.values()),
        labels =['Three Point Field Goals','2 Point Field Goals','Free Throws'],
        textprops=text, 
        explode = [0.2,0,0],
        autopct='%1.0f%%',
        shadow = 'on')
plt.title('Ray Allen: Point Breakdown',fontsize = 20, color='r', loc='center')

#Line chart of Points scored, assists

points = data.PTS
assists = data.AST
points
assists

plt.figure()
plt.plot(points,
     color='green',
     linestyle='dashed',
     linewidth=1)


plt.plot(assists,
     color='orange',
     linestyle='solid',
     linewidth=0.8)

plt.legend()
plt.xlabel('Game',fontsize = 12)
plt.ylabel("Value",fontsize = 12)
plt.grid(axis = 'both')
plt.title('Ray Allen: Assist and Point Log',fontsize = 20, color='y', loc='center')


#Assist/Point Scatter Plot
minutes = data.MP
for i in range(0,len(minutes)):
    minutes[i] = int(minutes[i][:2])

plt.figure()
plt.scatter(y = points,
            x = minutes)
plt.xlabel('Minutes Played',fontsize = 12)
plt.ylabel("Points Scored",fontsize = 12)
plt.grid(axis = 'both')
plt.title('Ray Allen: Minutes/Points',fontsize = 20, color='y', loc='center')








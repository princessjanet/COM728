"""
This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""

"""
Task 28 - 30: Write suitable functions to visualise the data as follows:

- Display the top 5 countries for confirmed cases using a pie chart
- Display the top 5 countries for death for specific dates using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country/countries.

Each function for the above should utilise the functions in the module 'database' to retrieve any data.
You may add additional methods to the module 'database' if needed. Each function should then visualise
the data using Matplotlib.
"""

# TODO: Your code here
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import database
import random

def func(pct,allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return"{:.1f}%\n({:d})".format(pct,absolute)
def pie_chart():
    records=database.retrieve_top_confirmed()
    lbs =[r[3] for r in records]
    data = [int(r[5]) for r in records]
    explode = (0.1,0.2,0.3,0.4,0.5)
    colors = ("orange", "cyan", "blue",
          "grey", "black")
    fig,ax = plt.subplots(figsize=(10,7))
    wedges,texts,autotexts =ax.pie(data,
                                    autopct = lambda pct: func(pct, data),
                                    explode = explode,
                                    labels = lbs,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    textprops = dict(color ="magenta"))
    ax.legend(wedges,lbs,
              title="countries",
              loc="center left",
              bbox_to_anchor= (1,0,0.5,1))
    plt.setp(autotexts,size =8, weight ="bold")
    ax.set_title("Top 5 Countries of confirmed cases")
    plt.show()


def bar_chart():
    records = database
    date = records[0][1]
    lbs = [r[3] for r in records]
    data = [int(r[6]) for r in records]
    fig = plt.figure(figsize=(10,5))
    plt.bar(lbs,data,color = 'purple',
            width = 0.4)
    plt.xlabel("countries")
    plt.ylabel("No of death")
    plt.title(f"Top 5 Countries with Deaths\nWith in {date}")
    plt.show()

global x1,x2,x3,y1,y2,y3,t1,t2,t3,confirmed,yb,yc,ax1,ax2,ax3,dates
def animate_confirmedcases(i):
    global x1,y1,confirmed,ax1,dates
    try:
        x1.append(dates[i])
        y1.append(confirmed[i])
        ax1.plot(x1, y1, scaley=True, scalex=True, color="green")
    except:
        pass
def animate_death(i):
    global x2,y2,ax2,dates,deaths
    try:
        x2.append(dates[i])
        y2.append(deaths[i])
        ax2.plot(x2, y2, scaley=True, scalex=True, color="red")
    except:
        pass
def animate_recovery(i):
    global x3, y3, ax3, dates, recovery
    try:
        x3.append(dates[i])
        y3.append(recovery[i])
        ax3.plot(x3, y3, scaley=True, scalex=True, color="blue")
    except:
        pass
def animate():
    global x1, x2, x3, y1, y2, y3, confirmed, yb, yc, ax1, ax2, ax3, dates, recovered, deaths
    plt.style.use("seaborn")
    region = input('what country/region?:')
    date = database.retrieve_summaryby(region)
    confirmed =[int(rec[1]) for rec in data]
    dates = [int(rec[0].split('/')[1]) for rec in data]
    deaths = [int(rec[2]) for rec in data]
    recovered = [int(rec[3]) for rec in data]

    fig= plt.figure(figsize=(5,5))
    ax1 = fig.add_subplot(1,1,1)
    x1,y1 = [],[]
    m= max([10,max(confirmed)])
    ax1.set_ylim(0,m)
    ax1.set_xlim(22,31)
    plt.xlabel("Dates of January")
    plt.ylabel("No. of confirmed cases")
    plt.title(f"{region} Animated Report")
    ani1 = FuncAnimation(fig=fig, func=animate1, interval=500)
    plt.show()

    fig = plt.figure(figsize=(5, 5))
    ax2 = fig.add_subplot(1, 1, 1)
    x2, y2 = [], []
    m = max([10, max(confirmed)])
    ax2.set_ylim(0, m)
    ax2.set_xlim(22, 31)
    plt.xlabel("Dates of January")
    plt.ylabel("No. of deaths")
    plt.title(f"{region} Animated Report")
    ani2 = FuncAnimation(fig=fig, func=animate2, interval=500)
    plt.show()

    fig = plt.figure(figsize=(5, 5))
    ax3 = fig.add_subplot(1, 1, 1)
    x3, y3 = [], []
    m = max([10, max(confirmed)])
    ax3.set_ylim(0, m)
    ax3.set_xlim(22, 31)
    plt.xlabel("Dates of January")
    plt.ylabel("No. of Recoveries")
    plt.title(f"{region} Animated Report")
    ani3 = FuncAnimation(fig=fig, func=animate3, interval=500)
    plt.show()

if __name__ == '__main__':
    animate()
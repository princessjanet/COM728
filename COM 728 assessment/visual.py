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
import numpy as np

def func(pct,allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return"{:.1f}%\n({:d})".format(pct,absolute)
def pie_chart():
    records=database.
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
    records= database
    date = records[0][1]
    lbs = [r[3] for r in records]
    data= [int(r[6]) for r in records]
    fig = plt.figure(figsize=(10,5))
    plt.bar(lbs,data,color = 'purple',
            width = 0.4)
    plt.xlabel("countries")
    plt.ylabel("No of death")
    plt.title(f"Top 5 Countries with Deaths\nWith in {date}")
    plt.show()


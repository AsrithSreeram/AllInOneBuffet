import pandas as pd
import matplotlib.dates as mdates

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

def getCovidVisualization():
    df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates=['Date'])
    df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

    #Worldwide Cases

    worldwide_df = df.groupby(['Date']).sum()
    w_chart = worldwide_df.plot(figsize=(10,7))
    w_chart.set_xlabel('Date')
    w_chart.set_ylabel('# of Cases WorldWide')
    w_chart.title.set_text('Covid-19 Visualization')
    plt.show()

    #United States vs.s Worldwide Cases and Deaths
    us_df = df[df['Country'] == 'US'].groupby(['Date']).sum()

    fig = plt.figure(figsize=(14,7))
    ax = fig.add_subplot(111)

    ax.plot(worldwide_df[['Total Cases']], label = "Worldwide")
    ax.plot(us_df[['Total Cases']], label = "United States")

    ax.set_xlabel('Date')
    ax.set_ylabel('# of Cases Total Cases')
    ax.title.set_text('World vs United States Total Cases')

    plt1.legend(loc = 'upper left')
    plt1.show()

    #Daily United States Cases and Deaths
    us_df = us_df.reset_index()
    us_df['Daily Confirmed'] = us_df['Confirmed'].sub(us_df['Confirmed'].shift())
    us_df['Daily Deaths'] = us_df['Deaths'].sub(us_df['Deaths'].shift())

    fig = plt.figure(figsize=(20,8))
    ax = fig.add_subplot(111)

    ax.bar(us_df['Date'], us_df['Daily Confirmed'], color='b', label='US Daily Confirmed Cases')
    ax.bar(us_df['Date'], us_df['Daily Deaths'], color='r', label='US Daily Deaths')

    ax.set_xlabel('Date')
    ax.set_ylabel('# of Cases and Deaths')

    ax.title.set_text('US Daily Cases and Deaths')
    plt2.legend(loc='upper left')

    plt2.show()

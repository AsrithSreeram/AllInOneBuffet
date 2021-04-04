import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

def getStockPrediction():
    quandl.ApiConfig.api_key = 'jMaJ3W9QVE4hzDZsA1xB'
    user = input("Enter stock (EX: Apple = AAPL) you want to have predicted graph on: ")

    df = quandl.get("WIKI/" + user)
    df = df [['Adj. Close']]

    df['Adj. Close'].plot(figsize=(15,6), color = 'g')
    plt.legend(loc='upper left')
    plt.show()

    #Machine Learning Applied Now
    forecast = 730
    df['Prediction'] = df [['Adj. Close']].shift(-forecast)


    X = np.array(df.drop(['Prediction'], 1))
    X = preprocessing.scale(X)

    X_forecast = X[-forecast:]
    X = X[:-forecast]

    y = np.array(df['Prediction'])
    y = y[:-forecast]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf = LinearRegression()
    clf.fit(X_train, y_train)

    confidence = clf.score(X_test, y_test)
    print(confidence)

    forecast_predicted = clf.predict(X_forecast)


    dates = pd.date_range(start="2018-03-28", end="2020-03-26")
    plt.plot(dates, forecast_predicted, color='y')
    df['Adj. Close'].plot(color='g')
    plt.xlim(xmin=datetime.date(2017,3,26))
    plt.show()
    plt.savefig('static/images/StockPrediction.png')

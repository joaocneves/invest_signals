
import numpy as np
import pandas as pd

def simpleMovingAverage(ts, periods: int = 20):
    return ts.rolling(window=periods).mean()


def exponentialMovingAverage(ts, periods: int = 20):
    return ts.ewm(span=periods, min_periods=periods, adjust=False).mean()

if __name__ == "__main__":

    df = pd.DataFrame({'test': [0, 1, 2, 3, 4]})

    print('----- ORIGINAL DATA ------')
    print(df)
    print('----- SIMPLE MOVING AVERAGE ------')
    print(simpleMovingAverage(df, periods=2))
    print('----- EXPONENTIAL MOVING AVERAGE ------')
    print(exponentialMovingAverage(df, periods=2))
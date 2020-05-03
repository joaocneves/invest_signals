from yahoo_historical import Fetcher
from indicators import simpleMovingAverage, exponentialMovingAverage
import matplotlib.pyplot as plt


data_link = Fetcher("EDP.LS", [2007,1,1])
data = data_link.get_historical()

ts_date = data['Date']
ts_price = data['Close']


ts_sma = simpleMovingAverage(ts_price,periods=30)
ts_ema = exponentialMovingAverage(ts_price, periods=30)

print(ts_sma[200])
print(ts_ema[200])
print(data.iloc[200,:])

plt.plot(ts_price)
plt.plot(ts_sma)
plt.plot(ts_ema)
plt.ylabel('price')
plt.show()




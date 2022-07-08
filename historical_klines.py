import pandas as pd 
import numpy as np
from binance.client import Client

#initialize client
client = Client()

frame = pd.DataFrame(client.get_historical_klines("LUNAUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2019", "1 day ago utc"))
frame.columns = ['Time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore']
frame = frame[['Time','Open','High','Low','Close','Volume']]
frame.set_index('Time', inplace = True)
frame.index = pd.to_datetime(frame.index ,unit = 'ms')
frame = frame.astype(float)
print(frame.head(20))
#frame.to_csv('LUNA_USDT_30min.csv',sep = ',',encoding = 'utf-8')

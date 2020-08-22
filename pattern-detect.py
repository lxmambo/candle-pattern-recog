import talib
import yfinance as yf

data = yf.download("SPY",start="2016-01-01",end="2020-08-21")
print(data)


blackcrows = talib.CDL3BLACKCROWS(data['Open'], data['High'],data['Low'],data['Close'])
hammer = talib.CDLHAMMER(data['Open'], data['High'],data['Low'],data['Close'])
evening_star = talib.CDLEVENINGSTAR(data['Open'], data['High'],data['Low'],data['Close'])
engulfing = talib.CDLENGULFING(data['Open'],data['High'],data['Low'],data['Close'])
morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'],data['Low'],data['Close'])

data['Crows'] = blackcrows
data['Hammer'] = hammer
data['Evening Star'] = evening_star
data['Morning Star'] = morning_star
data['Engulfing'] = engulfing

crows_days = data[data['Crows'] !=0 ]
hammer_days = data[data['Hammer'] != 0]
evening_days = data[data['Evening Star'] != 0]
morning_days = data[data['Morning Star'] != 0]
engulfing_days = data[data['Engulfing'] != 0]

print(engulfing_days)
print(morning_days)
print(evening_days)
print(hammer_days)
print(crows_days)
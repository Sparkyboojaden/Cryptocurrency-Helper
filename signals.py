from tradingview_ta import TA_Handler, Interval, Exchange
from robinhood import bp
import time

def get_current_price(ticker):
    #foreach ticker in tickers list
    ticker += "usdt"
    val = TA_Handler(
        #https://gyazo.com/b639194cc9ad9e8a03393983e71f221e <--- details via documentation on symbol, screener and exchange
        symbol = ticker, 
        screener="crypto", 
        exchange="binance",
        #list of intervals can be found here = https://gyazo.com/4badb0f2d0f28b9923d737d83281c890
        interval=Interval.INTERVAL_1_MINUTE 
    )
    return val.get_analysis().indicators['open']

#Replace this with a bot command that prints out the value in a channel


#Checks if the RSI value is between 70 and 30, if it is, it returns true, if the value is less than 30 or greater than 70 it returns false
def RSI_Check(tv):
    if(tv > 24 and tv < 80):
        return False #if the rsi is in a normal state
    else:
        return True # if the rsi is out of the expected range, print it

#Calculates the RSI of each ticker
def RSI_Calc(ticker):
    #foreach ticker in tickers list
    val = TA_Handler(
        #https://gyazo.com/b639194cc9ad9e8a03393983e71f221e <--- details via documentation on symbol, screener and exchange
        symbol = ticker, 
        screener="crypto", 
        exchange="binance",
        #list of intervals can be found here = https://gyazo.com/4badb0f2d0f28b9923d737d83281c890
        interval=Interval.INTERVAL_15_MINUTE 
    )
    #creates a dictionary for the bot to get the needed values
    ticker_info = dict()
    ticker = ticker[:-4]
    ticker_info["ticker_name"] = ticker
    ticker_info["ticker_rsi"] = val.get_analysis().indicators['RSI'] #gets ticker rsi
    #gets ticker price currently
    ticker_info["ticker_price"] = val.get_analysis().indicators['open']
    print(ticker_info)

    if(RSI_Check(ticker_info["ticker_rsi"]) == True):
        return ticker_info
    else:
        return "nothing" #This is used to let the call from the bot know if it should post or not



#for i in range(2):
#    RSI_Calc(tickers)
#    time.sleep(20)



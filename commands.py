from tradingview_ta import TA_Handler, Interval, Exchange
import time

#called from Bot.py
def crypto_stats(ticker):
    val = TA_Handler(
        symbol = ticker, 
        screener="crypto", 
        exchange="binance",
        interval=Interval.INTERVAL_1_DAY
    )
    ticker_value = val.get_analysis().indicators['RSI']
    ticker_open = val.get_analysis().indicators['open']
    ticker_close = val.get_analysis().indicators['close']

    vals = dict()
    vals["open"] = ticker_open
    vals["close"] = ticker_close
    vals["rsi_val"] = ticker_value


    return vals


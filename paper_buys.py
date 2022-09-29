import time
import datetime
import mysql.connector
from db_connection import mydb
from signals import * #get_current_price


#where we do all the executions
mycursor = mydb.cursor()

def is_table_empty():
    sql = "SELECT COUNT(*) FROM Buys"
    mycursor.execute(sql)
    row = mycursor.fetchone()
    return int(row[0])

def get_new_buy_id():
    sql = "SELECT BuyID from Buys ORDER BY BuyID DESC LIMIT 1"
    mycursor.execute(sql) # runs the command to find the last added buyID
    row = mycursor.fetchone()
    if(is_table_empty() == 0): #meaning we have an empty table (no rows)
        return 1
    else:
        #Used to format the result to just be a value and then returns the next free buyID
        loc = int(row[0]) + 1
        return loc

def close_position(bid, price):
    sql = "UPDATE Buys SET Sell_Price = (%s) WHERE BuyID = (%s)"
    vals = (price, bid)
    mycursor.execute(sql, vals)
    mydb.commit()
    print("Position closed", bid)

def make_a_buy(ticker, bp):
    btime = datetime.datetime.now()
    BID = get_new_buy_id()
    print("Opening a position", BID)
    sql = "INSERT INTO Buys (BuyID, Ticker, Buy_Price, Time) VALUES (%s, %s, %s, %s)"
    vals = (BID, ticker, bp, btime)
    mycursor.execute(sql, vals)
    mydb.commit()

    time.sleep(60)
    price = get_current_price(ticker)

    close_position(BID, price)

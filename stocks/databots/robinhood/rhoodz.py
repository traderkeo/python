import requests
import robin_stocks as rs
from datetime import timedelta, datetime
import time
from time import sleep
import pandas as pd


class account:
    def __init__(self,username,password):
        rs.authentication.login(username = f'{username}', password= f'{password}',store_session=True)





class rh:
    def __init__(self,login,password):
        print()


    def get_stock_price(self, stock_search):
        user_stock_search = stock_search
        user_stock_price = rs.stocks.get_latest_price(user_stock_search)
        user_stock_price_int = float(user_stock_price[0])
        return user_stock_price_int
    
   
    
    def get_fundamentals(self,tickers,info):
        i = info
        t = tickers
        ob = {}
        li = [rs.stocks.get_fundamentals(tickers,i[x]) for x in range(len(i))]
        df = toDF([li,i,t])
        df['v_ratio'] = [ratio(df.iloc[x][0],df.iloc[x][1]) for x in range(len(df))]
        return df
    
    
    def get_vols(self,tickers):
        i =  ['volume','average_volume']
        t = tickers
        ob = {}
        li = [rs.stocks.get_fundamentals(tickers,i[x]) for x in range(len(i))]
        df = toDF([li,i,t])
        df['v_ratio'] = [ratio(df.iloc[x][0],df.iloc[x][1]) for x in range(len(df))]
        df['gain'] = rh('kkkka','sadsadas').get_gain(t)
        return df
    
    def get_vol(self, tickers):
        t = tickers
        ob = {}
        li = rs.stocks.get_fundamentals(tickers,info='volume') 
        return li
    
    def get_average_vol(self, tickers):
        t = tickers
        ob = {}
        li = rs.stocks.get_fundamentals(tickers,info='volume') 
        return li
    
    
    def get_quote(self,ticker):
        return rs.stocks.get_quotes(ticker)
        
    def get_gain(self,ticker):
        i = ['last_trade_price','previous_close']
        lp = []
        lt = []
        
        lp.append(rs.stocks.get_quotes(ticker,info=f"{i[0]}"))
        lt.append(rs.stocks.get_quotes(ticker,info=f"{i[1]}"))
        #r = ratio(r[0][0],r[1][0])
        #print(f'{round(r,2)*100}%')
        lp = lp[0]
        lt = lt[0]
        t = [gain(lp[x],lt[x]) for x in range(len(lp))]
        return t
    
    def keys(self):
        print(""" 
            open
            high
            low
            volume
            average_volume_2_weeks
            average_volume
            high_52_weeks
            dividend_yield
            float
            low_52_weeks
            market_cap
            pb_ratio
            pe_ratio
            shares_outstanding
            description
            instrument
            ceo
            headquarters_city
            headquarters_state
            sector
            industry
            num_employees
            year_founded
            symbol
              """)
              
              
def toDF(self):
        d = self
        df=pd.DataFrame()
        for x in range(len(d[1])):
            label = d[1][x]
            df[label] = d[0][x]
            
        df['tickers'] = d[2]
        return df
    
    
    
def ratioDF(self):
    d = self
    arr = []
    for x in range(len(d)):
        try:
            arr.append(d[['volume','average_volume']].iloc[x][0], ratio(d[['volume','average_volume']].iloc[x][1]))
        except:
            arr.append(0)
    d['vol_ratio'] = arr
    return d



def ratio(start,final):
    return float(start)/float(final)
    

def gain(start,finish):
    if start > finish:
       return round((float(start)/float(finish))-1,3)
    else:
       return round((1-(float(start)/float(finish)))*-1,3)

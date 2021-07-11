import requests
import pandas as pd
from random import seed
from random import randint
from bs4 import BeautifulSoup
import time
import json
from redditStocks import reddit


pd.set_option('display.max_rows', None)

class vizStats:
    def relativeVolume():
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
                
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        
        
        
        r = requests.get('https://finviz.com/screener.ashx?v=111&f=sh_relvol_o10', headers=headers)
        
        soup = BeautifulSoup(r.text,"lxml")
        
        df = pd.read_html(str(soup.find(id="screener-content").find('table')))[3]
        labels = list(df.iloc[0])
        df = df[1:]
        df.columns = labels
        return df
    
    
    def freeFloat(self,t):
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
                
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        
        dfList = []
        
        r = requests.get(f'https://finviz.com/screener.ashx?v=111&f=sh_float_u{self}', headers=headers)
        soup = BeautifulSoup(r.text,"lxml")
        maxPages = len(soup.find(id="pageSelect").find_all('option'))
        df = pd.read_html(str(soup.find(id="screener-content").find('table')))[3]
        labels = list(df.iloc[0])
        df = df[1:]
        df.columns = labels
        dfList.append(df)
        
        for x in range(maxPages):
            try:
                print(x)
                headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
                seed(1)
                    
                headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
                if x >= 1:
                    r = requests.get(f'https://finviz.com/screener.ashx?v=111&f=sh_float_u{self}&r={x+20}', headers=headers)
                else:
                    r = requests.get(f'https://finviz.com/screener.ashx?v=111&f=sh_float_u{self}&r={x+21}', headers=headers)
            
                soup = BeautifulSoup(r.text,"lxml")
                
                df = pd.read_html(str(soup.find(id="screener-content").find('table')))[3]
                labels = list(df.iloc[0])
                df = df[1:]
                df.columns = labels
                dfList.append(df)
            except:
                pass
            
    
        finDF = pd.concat(dfList,ignore_index=True)
        finDF = finDF.drop_duplicates()
        
        if t == 'reddit':
            li = list(finDF['Ticker'])
            red = [reddit(li[x],'agg') for x in range(len(li))]
            finDF['comments'] = [red[x][1] for x in range(len(red))]
            finDF['upvotes'] = [red[x][0] for x in range(len(red))]
            return finDF
        else:
            return finDF
        
    
    def optionable():
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
                
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        
        dfList = []
        
        r = requests.get(f'https://finviz.com/screener.ashx?v=111&f=sh_opt_option&r=', headers=headers)
        soup = BeautifulSoup(r.text,"lxml")
        maxPages = len(soup.find(id="pageSelect").find_all('option'))
        df = pd.read_html(str(soup.find(id="screener-content").find('table')))[3]
        labels = list(df.iloc[0])
        df = df[1:]
        df.columns = labels
        dfList.append(df)
        
        for x in range(5):
                print(x)
                headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
                seed(1)
                    
                headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
                if x >= 1:
                    r = requests.get(f'https://finviz.com/screener.ashx?v=111&f=sh_opt_option&r={x+20}', headers=headers)
                else:
                    r = requests.get(f'https://finviz.com/screener.ashx?v=111&f=sh_opt_option&r={x+21}', headers=headers)
            
                soup = BeautifulSoup(r.text,"lxml")
                
                df = pd.read_html(str(soup.find(id="screener-content").find('table')))[3]
                labels = list(df.iloc[0])
                df = df[1:]
                df.columns = labels
                dfList.append(df)
            
            
    
        finDF = pd.concat(dfList,ignore_index=True)
        finDF = finDF.drop_duplicates()
        return finDF
    
    
    def quote(self):
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
                
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        
        
        
        r = requests.get(f'https://finviz.com/quote.ashx?t={self}', headers=headers)
        soup = BeautifulSoup(r.text,"lxml")
        labels =  soup.find_all('td',{'class':'snapshot-td2-cp'})
        labels = [labels[x].text for x in range(len(labels))]
        data = soup.find_all('td',{'class':'snapshot-td2'})
        data = [data[x].text for x in range(len(data))]
        df = pd.DataFrame()
        df[0] = labels
        df[1] = data
        df = df.set_index(0)
        
        return df
    
class vizStrat:
    
    def scan(strat,floats):
        if strat == "trend resistance":
            a = 'tlresistance'
        elif strat == "horizontal":
            a = 'horizontal'
        elif strat == "trend support":
            a = 'tlsupport'
        elif strat == "wedge up":
            a = 'wedgeup'
        elif strat == "wedge down":
            a = 'wedgedown'
        elif strat == "wedge resistance":
            a = 'wedgeresistance'
        elif strat == "wedge support":
            a = 'wedgesupport'
        elif strat == "wedge":
            a = 'wedge'
        elif strat == "channel up":
            a = 'channelup'
        else:
            return print(" ~| wedge support |~~| wedge down |~ ~| trend resistance |~~| trend support |~ ~| horizontal |~~| wedge up |~ ~| wedge resistance |~~| channel up |~~| wedge |~")
        
        
        if floats > 100:
            floats = 100
            
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
                
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        le = [1]
        url = f'https://finviz.com/screener.ashx?v=111&f=sh_float_u{floats},sh_opt_option,ta_pattern_{a}2&ft=4&r='
        
        r = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(r.text,"lxml")
        maxPages = len(soup.find(id="pageSelect").find_all('option'))
        
        dataList = []    
        news = []
        for x in range(maxPages):
            num = le[-1] + 20
            le.append(num)
            print(le[-1])
            print(f'!~~ {x} / {maxPages} ~~!')
            headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
            seed(1)
            url = f'https://finviz.com/screener.ashx?v=111&f=sh_float_u{floats},sh_opt_option,ta_pattern_{a}2&ft=4&r={le[-1]}'
            print(url)   
            headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
            r = requests.get(url, headers=headers)
            
            soup = BeautifulSoup(r.text,"lxml")
            df = pd.read_html(str(soup.find(id="screener-content").find('table')))[3]
            
            
            labels = list(df.iloc[0])
            df = df[1:]
            df.columns = labels
            #print(df)
            
            dataList.append(df)
           
        
       
        df = pd.concat(dataList,ignore_index=True)
        df = df.drop_duplicates()
        return df
    

    #f"https://charts2.finviz.com/chart.ashx?s=m&t={self}"

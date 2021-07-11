import requests
import pandas as pd
from random import seed
from random import randint
from bs4 import BeautifulSoup
import time
import json
from sqliteDF import sql




    
    
    
class screener:
    def checkOptions():
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        url = 'https://finviz.com/screener.ashx?v=111&ft=4'
        
        r = requests.get(url,headers=headers)
        
        soup = BeautifulSoup(r.text, "lxml")
        
        
        data = soup.find('td',{'class':'filters-border'})
        
        selects = data.find_all('select')
        
        urls = [selects[x].attrs['data-url-selected'] for x in range(len(selects))]
        urls = [urls[x].split('111')[1]+"&" for x in range(len(urls))]
        optionText = [data.find_all('span')[x].text for x in range(len(data.find_all('span')))]
        options = [[selects[x].find_all('option')[a].attrs['value'] for a in range(len(selects[x].find_all('option')))] for x in range(len(selects))]
        optionNames = [[selects[x].find_all('option')[a].text for a in range(len(selects[x].find_all('option')))] for x in range(len(selects))]
        
        df = pd.DataFrame()
        df['urls'] = urls
        df['optionText'] = optionText
        df['options'] = options
        df['optionNames'] = optionNames
    
    
    def  __init__(self, types):
        if types == 'options':
            self._options = screener.checkOptions()
            self._labels = [self._options['optionText'][x] for x in range(len(self._options))]

    def filters(self):
         options = self._options
         labels = [options['optionText'][x] for x in range(len(options))]
         options = [options['options'][x] for x in range(len(options))]
         res = [str(labels[x])+" "+str(options[x]) for x in range(len(options))]
         return print(res)
     
    
    def filterOptions(self, text):
         options = self._options
         return list(options[options['optionText'] == text]['optionNames'])
     

        


    def filterURL(self,type, op):
        ss = self._options
        ll = ss[ss['optionText'] == type].iloc[0]['urls']
        _df = pd.DataFrame()
        _df['label'] = str(ss[ss['optionText'] == type].iloc[0]['optionNames']).split(',')
        _df['label'] = [_df['label'].iloc[x].strip().replace("'","") for x in range(len(_df))]
        _df['labelURL'] = str(ss[ss['optionText'] == type].iloc[0]['options']).split(',')
        _df['labelURL'] = [_df['labelURL'].iloc[x].strip().replace("'","") for x in range(len(_df))]
        
        d = _df[_df['label'] == op].iloc[0]['labelURL']
        return f'https://finviz.com/screener.ashx?v=111{ll.replace("selected_filter",d)}r='
    
    
def results(url):
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
                
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        le = [0]
        url = url
        
        r = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(r.text,"lxml")
        maxPages = len(soup.find(id="pageSelect").find_all('option'))
        
        dataList = []    
        news = []
        for x in range(maxPages):
            
            print(le[-1])
            print(f'!~~ {x} / {maxPages} ~~!')
            headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
            seed(1)
            url2 = url + str(le[-1])
          
            
            if x == 0:
                le.append(21)
            else:
                le.append(le[-1]+20)
            
            print(url2)   
            headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
            r = requests.get(url2, headers=headers)
            
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

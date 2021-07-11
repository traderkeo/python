import requests
import json
from random import seed
from random import randint
import time
import pandas as pd
from datetime import datetime

def tester(self):
        print(aft[-1])        
        headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
        seed(1)
            
        headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
        
        r = requests.get(f'https://www.reddit.com/search.json?q={self}&type=link&t=week&after=' + aft[-1],headers=headers)
        print(r)
        data = json.loads(r.text)
        
        
        
        
        after = data["data"]["after"]
        print(after)
        posts = data["data"]["children"]
        
       
        dataList = []
        for i in range(len(posts)):
            keys = [key for key in posts[i]['data']]
            data = [posts[i]['data'][keys[x]] for x in range(len(keys))]
                
                
            df = pd.DataFrame()
            df['keys'] = keys
            df['data'] = data
            df = df.set_index('keys').transpose()
            dataList.append(df)
            aft.append(after)
        ddd = pd.concat(dataList,ignore_index=True)
        print(len(ddd))
        masterData.append(ddd)
            
        return False;
    
def reddit(self,t):
    aft = ['null']
    masterData = []
    try:
        while True:
            if aft[-1] != 'None':
                
                print(aft[-1])        
                headerlist = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
                seed(1)
                    
                headers = {'user-agent': headerlist[randint(0, len(headerlist))]}
                
                r = requests.get(f'https://www.reddit.com/search.json?q={self}&type=link&t=week&after=' + aft[-1],headers=headers)
                print(r)
                data = json.loads(r.text)
                
                
                
                
                after = data["data"]["after"]
                print(after)
                posts = data["data"]["children"]
                
               
                dataList = []
                for i in range(len(posts)):
                    keys = [key for key in posts[i]['data']]
                    data = [posts[i]['data'][keys[x]] for x in range(len(keys))]
                        
                        
                    df = pd.DataFrame()
                    df['keys'] = keys
                    df['data'] = data
                    df = df.set_index('keys').transpose()
                    dataList.append(df)
                    aft.append(after)
                ddd = pd.concat(dataList,ignore_index=True)
                print(len(ddd))
                masterData.append(ddd)
            else:
                break
    except:
        if t == 'table':
            try:
                md = pd.concat(masterData,ignore_index=True)
                md['created_utc'] = [datetime.utcfromtimestamp(md['created_utc'][x]).strftime('%m-%d-%Y') for x in range(len(md))]
                m2 = md[['created_utc','ups','num_comments','num_crossposts']].groupby('created_utc').sum()
                try:
                    m2['up_increase'] = [0,] + [str(round(((m2['ups'][x+1] - m2['ups'][x])/m2['ups'][x])*100))+" %" for x in range(len(m2)-1)]
                    m2['comments_increase'] = [0,] + [str(round(((m2['num_comments'][x+1] - m2['num_comments'][x])/m2['num_comments'][x])*100))+" %" for x in range(len(m2)-1)]
                    return m2, sum(m2['ups']),sum(m2['num_comments'])
                except:
                    return m2, sum(m2['ups']),sum(m2['num_comments'])
            except:   
                return 'error',0,0
            
           
        elif t == 'agg':
            try:
                md = pd.concat(masterData,ignore_index=True)
                md['created_utc'] = [datetime.utcfromtimestamp(md['created_utc'][x]).strftime('%m-%d-%Y') for x in range(len(md))]
                m2 = md[['created_utc','ups','num_comments','num_crossposts']].groupby('created_utc').sum()
                return  sum(m2['ups']), sum(m2['num_comments'])
            except:
                return 0,0


#md = pd.concat(masterData,ignore_index=True)

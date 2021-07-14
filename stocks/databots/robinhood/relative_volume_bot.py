import requests
from datetime import timedelta, datetime
import time
from time import sleep
from rhoodz import rh,account
import pandas as pd


class rv_bot:
    def __init__(self,tickers):
            #self._account = account('nimraw23','KeonSynack@020')
            self._start = time.perf_counter()
            self._df = rh('null','null').get_vols(tickers)
            self._tickers = list(self._df['tickers'])
            self._gain = self._df['gain']
            self._avVol = self._df['average_volume']
            print(f'The following stocks have been initialized {self._tickers}')
        
    def vol(self):
        return rh('kkkka','sadsadas').get_vol(self._tickers)
    
    def avgs(self):
        vol = rh('kkkka','sadsadas').get_vol(self._tickers)
        vol = [float(vol[x]) for x in range(len(vol))] 
        avgs = list(self._avVol)
        avgs = [float(avgs[x]) for x in range(len(avgs))] 
        rel = [round(utils.ratio(vol[x],avgs[x]),1) for x in range(len(avgs))]
        indexes = [i for i in range(len(rel)) if rel[i] >= 5]
        #[self._tickers[indexes[x]] for x in range(len(indexes))]
        return indexes
    
    def rel(self):
        vol = rh('kkkka','sadsadas').get_vol(self._tickers)
        vol = [float(vol[x]) for x in range(len(vol))] 
        avgs = list(self._avVol)
        avgs = [float(avgs[x]) for x in range(len(avgs))] 
        rel = [round(utils.ratio(vol[x],avgs[x]),1) for x in range(len(avgs))]
        #indexes = [i for i in range(len(rel)) if rel[i] >= 5]
        #[self._tickers[indexes[x]] for x in range(len(indexes))]
        return rel
        
    def pumping(self):
        vol = rh('kkkka','sadsadas').get_vol(self._tickers)
        vol = [float(vol[x]) for x in range(len(vol))] 
        avgs = list(self._avVol)
        avgs = [float(avgs[x]) for x in range(len(avgs))] 
        rel = [round(utils.ratio(vol[x],avgs[x]),1) for x in range(len(avgs))]
        indexes = [i for i in range(len(rel)) if rel[i] >= 5]
        
        return [self._tickers[indexes[x]] for x in range(len(indexes))]
    
    def timecheck(self):
        return utils.timer(self._start)

class utils:       
    def timer(start):
        toc = time.perf_counter()
        d = toc - start
        print(d)
        return d
    
    def time():
        t = datetime.now().strftime('%I.%M %p').split(' ')
        if t[-1] == 'PM':
            n = t[0].split('.')
            return ".".join([str(int(n[0])+12),n[1]])
        else:
            return t[0]
        
    def captime():
            cap_time = datetime.now()
            cap_time_form = cap_time.strftime("%d-%b-%Y %I.%M.%S %p")
            #cap_time_form = cap_time.strftime("%d-%b-%Y %H.%M.%S")
            return cap_time_form

    def ratio(start,final):
        return float(start)/float(final)


class bot_manager:
    def __init__(self,tickers):
        self._tickers = tickers
        self._timestart = '05:30'
        self._marketOpen = '13:00'
        self._timer = time.perf_counter()
        self._databank = []
        self._bot = rv_bot(tickers)
        
        
    def check(self):
        aa = self._bot.vol()
        aa2 = self._bot.avgs()
        rh('kkkka','sadsadas').get_cap_time()
        self._df
        
    def update(self):
        masterFrame = pd.DataFrame()
        masterFrame['ticker'] = self._tickers
        masterFrame['ratio'] = self._bot.rel()
        masterFrame = masterFrame.set_index('ticker').transpose()
        masterFrame.index = [utils.captime()]
        print(masterFrame)
        self._databank.append(masterFrame) 
    def data(self):
        return pd.concat(self._databank,ignore_index=False)
        

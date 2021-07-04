import requests
from bs4 import BeautifulSoup
import pandas as pd
from unicodedata import normalize
from ezemail import email


pd.set_option('display.max_columns', None)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',

    }

dfs = []

for x in range(5):
    r = requests.get(f'https://fintel.io/activists?page={x}')
    soup = BeautifulSoup(r.text,"lxml")
    data = soup.find(id="topic-table-body")
    df = pd.read_html(str(data.find('table')))[0]
    dfs.append(df)

    
master = pd.concat(dfs,ignore_index=True)
master = master.drop_duplicates()
nn = []
for x in range(len(master)):
    try:
        nn.append(master.iloc[x]['Target'].split('/')[0].strip())
    except:
        nn.append(master.iloc[x]['Target'])
master['Target'] = nn
master = master[master['Target'] != ""]
master['ps'] = [pd.isna(master.iloc[x]['PreviousShares']) for x in range(len(master))]
nn = master[master['ps'] == True]

mm = nn.groupby('Target').size().reset_index().drop_duplicates()
top = mm.sort_values(0, ascending=False)
top['Target'] = [top.iloc[x]['Target'].split('/')[0].strip() for x in range(len(top))]
top = top.reset_index(drop=True)[0:10]
top.columns = ['Ticker','Activist Positions Taken']
##ndf = pd.concat([df[0],df2[0]],ignore_index=True)
nn = master[master['ps'] == True]
own = master[master['Ownership Change(Percent)'] >= 0.1]

totalNewPositions = master.groupby('Date').size()
totalNewPositions.columns = ['date','total positions taken']
tp = pd.DataFrame(totalNewPositions)
tp.columns = ['New Positions Taken']

li = li.sort_values(0, ascending=False)
li = master.groupby('Lead Investor').size()
li = pd.DataFrame(li)
li.columns = ['New Positions Taken']


html = """ <table border="0" class="text-row-single"><tr><p>Top Stocks With Brand New Activist Positions</p></tr></table> """ + top.to_html(index=False,sparsify=True,justify='center',col_space='100px') + """
<table border="0" class="text-row-single"><tr><p>How Many Activist Positions Were Taken This Week?><p></tr></table>
""" + tp.to_html(sparsify=True,justify='center',col_space='50px') + """Who are the most active activist investors?""" + li[0:10].to_html(sparsify=True,justify='center',col_space='50px')


email.html(['******','*****'],'Activest Investments - ArminFinance',html)

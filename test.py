import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os ##to create new directories
import pandas as pd
import pandas_datareader.data as web
#import fix_yahoo_finance
import pickle ##serializes python object, can save any object, we're going to save s&p500 list
import requests
nt = list()
def save_nasdaq_name_and_ticker():
    resp = requests.get('http://www.nasdaqomxnordic.com/aktier/listed-companies/stockholm')
    soup = bs.BeautifulSoup(resp.text, "lxml") ##resp.txt is text fo source code, 2 is how parsing
    table = soup.find('table', {'class':'tablesorter'}) ##specifies which table
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        name = row.findAll('td')[0].text
        #ticker = ticker.replace(' ','-')
        #ticker = ticker + '.ST'
        nt.append([name, ticker])
    #print(nt)
        #tickers.append(ticker)
    with open("nasdaqnamesandticker.pickle", "wb") as f:
        pickle.dump(nt, f) ##dumping tickers to file f
#    print(tickers)
    #return tickers
#save_nasdaq_name_and_ticker()

#with open("nasdaqnames.pickle", "rb") as f:
#    names = pickle.load(f)
#    for name in names:
#        print(name)
pickle_names = pickle.load(open('nasdaqnames.pickle', 'rb'))
pickle_tickers = pickle.load(open('nasdaqtickers.pickle', 'rb'))

names_and_tickers = pickle_names
names_and_tickers.append(pickle_tickers)

#for line in names_and_tickers:
#    print(line)
def percentage_change():
    with open("nasdaqnamesandticker.pickle", "rb") as f: ##wb is write bytes, rb is read bytes
        nat = pickle.load(f) ##think we got the ticker list
        #print(tickers) OK
        start = dt.datetime(2015,1,1)
        end = dt.datetime(2016,1,1)
        #df = web.DataReader('ASSA-B.ST', 'yahoo', start, end)
        for lst in nat:
            #print(ticker)
            ticker = lst[1]
            ticker = ticker.replace(' ', '-')
            ticker = ticker + '.ST'
            df = web.get_quote_yahoo(ticker)
            df.drop(['PE', 'short_ratio'],1, inplace=True)
            name = lst[0]
            #print(df.head())
            requirement = 2.00
            #if df(['change_pct'] > abs(requirement):
            s = df['change_pct']
            #if df.iloc[lambda df: df.change_pct > abs(requirement)]:
            #print(s)
            #df.iloc[0]
            df['change_pct'] = pd.to_numeric(df['change_pct'].str.replace('%', ''))#.str.replace('+', '').str.replace('-', ''))
            #print(df.dtypes)
            #if df.loc[lambda df: df.change_pct > abs(requirement)]:
            for num in df['change_pct']:
                if num > requirement:
                    print('Buy: ', name, ticker, num)
            #if df['change_pct'] > requirement:
                #print(df)
            #if df.loc[df['change_pct'] > 2,'change_pct']:
            #    print(df)

            #result = result[]
percentage_change()

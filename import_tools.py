import numpy as np
import matplotlib.pyplot as plt
import bs4 as bs
import datetime as dt
import os ##to create new directories
import pandas as pd
import pandas_datareader.data as web
import pickle ##serializes python object, can save any object, we're going to save s&p500 list
import requests

class data_import():
    def __init__(self):
        self.stocklist = []

        print('Initializing import class')

    def save_nasdaq_stocklist(self, stockexchange='stockholm'):
        resp = requests.get('http://www.nasdaqomxnordic.com/aktier/listed-companies/' + stockexchange)
        soup = bs.BeautifulSoup(resp.text, "lxml") ##resp.txt is text fo source code, 2 is how parsing
        table = soup.find('table', {'class':'tablesorter'}) ##specifies which table
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[1].text
            name = row.findAll('td')[0].text
            icb = row.findAll('td')[5].text
            self.stocklist.append([name, ticker, icb])

        with open('stocklist.txt', 'w') as textfile:
            for line in self.stocklist:
                string = ''
                for element in line:
                    string = string + element + ','
                string = string[:-1]
                textfile.write(string + '\n')

        self.stocklist = []

    def load_stocklist(self):
        with open('stocklist.txt', 'r') as textfile:
            for line in textfile:
                line = line.rstrip('\n')
                line = line.split(',')
                self.stocklist.append(line)
        self.stocklist = np.asarray(self.stocklist)

    def parse_stock_data(self, ticker, database='yahoo'): #database='yahoo' sets yahoo as default
        start = dt.datetime(2015, 1, 1)
        end = dt.datetime(2016, 1, 1)

        ticker_save = ticker

        if not os.path.exists('data'): ##if this path does not exists
            os.makedirs('data')

        if database == 'yahoo':
            ticker = ticker.replace(' ','-')
            ticker = ticker + '.ST'

        try:
            if not os.path.exists('data/{}.csv'.format(ticker_save)):
                df = web.DataReader(ticker, database, start, end)
                print(df)
                df.to_csv('data/{}.csv'.format(ticker_save))

            else:
                print('Already have {}'.format(ticker_save))
        except Exception as e:
            print(e)
            print('\n Failed:', ticker_save)

    def load_stock_data(self, ticker):
        data = []
        timestamps = []
        if os.path.exists('data'):
            print('data/' + ticker + '.csv')
            with open('data/' + ticker + '.csv') as textfile:
                next(textfile)
                for line in textfile:
                    line = line[:-2]
                    line = line.split(',')
                    timestamps.append(line[0])
                    line = line[1:]

                    print(line)
                    try:
                        line = [float(el) for el in line]
                    except Exception as e:
                        line = [0]*len(line)
                        print(e)
                    data.append(line)
        data = np.asarray(data)
        return timestamps, data

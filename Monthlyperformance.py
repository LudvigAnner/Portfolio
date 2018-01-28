import numpy as np
import matplotlib.pyplot as plt
import bs4 as bs
import datetime as dt
import os  # to create new directories
import pandas as pd
import pandas_datareader.data as web
import pickle  # serializes python object, can save any object, we're going to save s&p500 list
import requests


class monthly_performance():
    def __init__(self):
        self.stocklist = []
        print('Initializing monthly performance')

    def open_stocklist(self):
        print('start')
        with open('stocklist.txt', 'r') as textfile:
            for row in textfile:
                ticker = line.rstrip('\n')
                ticker = line.split(',')
                ticker = ticker(1)
                print(ticker)

            # self.stocklist.append(line)
m = monthly_performance()

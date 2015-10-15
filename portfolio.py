'''Get a list of trades where trade is a tuple'''
import pprint
import csv
from collections import namedtuple

Trade = namedtuple('Trade', ['symbol' ,'shares', 'price'])

def get_portfolio(filename):
      trades = []
      with open(filename) as f:
            for symbol, shares, price in csv.reader(f):
                  trade = Trade(symbol, int(shares), float(price))
                  trades.append(trade)
      return trades


if __name__ == '__main__':
      port = get_portfolio('notes/stocks.txt')
      pprint.pprint(port)

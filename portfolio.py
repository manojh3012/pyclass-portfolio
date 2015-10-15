'''Get a list of trades where trade is a tuple'''
import pprint
from collections import namedtuple

Trade = namedtuple('Trade', ['symbol' ,'shares', 'price'])

def get_portfolio(filename):
      trades = []
      with open(filename) as f:
            for line in f:
                  line = line.rstrip()
                  symbol, shares, price = line.split(',')
                  trade = Trade(symbol, int(shares), float(price))
                  trades.append(trade)
      return trades


port = get_portfolio('notes/stocks.txt')
pprint.pprint(port)

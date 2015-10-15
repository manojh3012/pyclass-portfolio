'''Get a list of trades where trade is a tuple'''
import pprint
from collections import namedtuple

Trade = namedtuple('Trade', ['symbol' ,'shares', 'price'])

trades = []
with open('notes/stocks.txt') as f:
      for line in f:
            line = line.rstrip()
            symbol, shares, price = line.split(',')
            trade = Trade(symbol, int(shares), float(price))
            trades.append(trade)            


pprint.pprint(trades)

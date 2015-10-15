'''Get a list of trades where trade is a tuple'''

trades = []
with open('notes/stocks.txt') as f:
      for line in f:
            line = line.rstrip()
            symbol, shares, price = line.split(',')
            trade = symbol, int(shares), float(price)
            print trade
            trades.append(trade)            

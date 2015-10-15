'''Get a list of trades where trade is a tuple'''

with open('notes/stocks.txt') as f:
      for line in f:
            pass
#            print line


line = line.rstrip()
fields = line.split(',')
print fields

from operator import itemgetter

opeth = ['Burden', 'Hex Omega', 'Bridge of Sights', 'Windowpane', 'To Bid You Farewell', 'Isolation Years']
print (opeth)
count = opeth.count('Burden')
print (count)
count = opeth.count('Bridge of Sights')
print (count)

index = opeth.index('Bridge of Sights')
print (index)
index = opeth.index('Windowpane', 2)
print (index)

opeth.reverse()
print (opeth)

opeth.append('Snuff')
print (opeth)

opeth.sort()
print (opeth)

retirar_item = opeth.pop(4)
print (opeth.pop)
print(retirar_item)

IronMaiden = ['Wasted Years', 'Sea of Madness']
opeth.extend (IronMaiden)
print (opeth)

opeth.insert(0, 'Ending Credits')
print (opeth)

opeth.remove('Sea of Madness')
print(opeth)

opeth.clear()
print (opeth)

opeth.copy()
print (opeth)
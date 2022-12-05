'''
Prints out a randomized string of Pekora laughs.
The generated string can be posted into discord, where the asterisks 
will format the text to be *italic*, **bold**, or ***both***.
'''

from random import *

ha = [['ha','hA','Ha','HA']]
for i in range(3):
    ha.append(['*' + i + '*' for i in ha[-1]])
arr = ['↗️', '↘️']

min_ha, max_ha = [int(i) for i in input().split()]
n = randrange(min_ha, max_ha)
s = []

for i in range(n):
    s.append( choice(choice(ha)) )
    s.append( choice(arr) )

s = ' '.join(s)
print(s)

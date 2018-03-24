
import pandas as pd
def printMultiples(n):
    i = 1
    while i <= 6:
     print (n*i, '\t',)
     i = i + 1

def printMultTable(n):
    i = 1
    while i <= 6:
     printMultiples(i)
     i = i + 1



printMultiples(6)
printMultTable(10)

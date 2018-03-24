##import time
##
##for a in range(1,11):
##    print ("\n")
##    time.sleep(2)
##    for b in range(1,11):
##        print(a,"x",b,"=",a*b)
##
##def printtwice(maru5):
##    print "maru5 maru5"
##
##printtwice("maruti")
##
##
##print "produces","\n","\t","this","\n","\t","\t","output"

##
##def table(n):
##    i=1
##    while i<=7:
##        print n*i," ",
##        i=i+1
##    print
##    
##def tablem(n):
##    i=1
##    while i<=n:
##     table(i)
##     i=i+1
##     
##tablem(8)

def printMultiples(n, high):
    i = 1
    while i <= high:
     print n*i,"",
     i = i + 1
    print
def printMultTable(high):
    i = 1
    while i <= high:
     printMultiples(i, high)
     i = i + 1
printMultTable(7)

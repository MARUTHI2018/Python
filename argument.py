##def find(str, ch):
##    index = 0
##    while index < len(str):
##     if str[index] == ch:
##        return index
##      index = index + 1
##      print index
##     return -1

##
##
##
def find(str, ch, start=0):
    index = start
    while index < len(str):
     if str[index] == ch:
      print index
      return index
     index = index + 1
     
    return -1

find("apple","p",3)

##
##class Time:
####    def __init__(self, hours=0, minutes=0, seconds=0):
##    pass
####Time(9,12,11)
##
##
##    
##T1=Time()
##T1.hours = 9
##T1.minutes = 10
##T1.seconds = 12
####Printtime(currenttime)
###tag changes for demo commit
##
##    
##def time(T1):
##     sum=Time()
####     return self
##     sum.hours=T1.hours
##     sum.minutes=T1.minutes
##     sum.seconds=T1.seconds
##     return sum
####    print str(hours)+ ":" + str(minutes) +":"+str(seconds)
##

class Time:
    pass
##def printTime(time):
##     print str(time.hours)+ ":" + str(time.minutes) +":"+str(time.seconds)
####abc=time(T1)
####Printtime(abc)

currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30
##printTime(currentTime)

class Time:
    def printTime(time):
     print str(time.hours)+ ":" + str(time.minutes) +":"+str(time.seconds)
currentTime.printTime()
##
##class Time:
##    def __init__(self, hours=0, minutes=0, seconds=0):
##     self.hours = hours
##     self.minutes = minutes
##     self.seconds = seconds


##currentTime=self(9,14,30)

##currentTime.printtime()
























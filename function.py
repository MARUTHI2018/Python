
##printtwice("maruti")
##


def cattwice(part1, part2):
    cat = part1 + part2
    print (cat)
    printtwice(cat)


def printtwice(maru5):
    print maru5,maru5
    
chant1="aaa is good."
chant2="bee is bad."
cattwice(chant1, chant2)

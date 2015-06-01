import sys
import math

num = ''
for i in range(1,1000000):
    num = str(i)
    mylist = []
    for l in num:
        mylist.append(int(l))
    truth = 0
    if sum(mylist) == 43:
        if  math.pow(i,(1/2.0)).is_integer() == True:
            truth +=1
        if math.pow(i,(1/3.0)).is_integer() == True:
            truth +=1
        if float(i) < 500000:
            truth +=1
    if truth == 2:
        winner = i
        print "winner :" + str(winner)
        sys.exit

string = "xyza"

alpha = "abcdefghijklmnopqrstuvwxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vow = "aeiouAEIOU"

newstr = ""

for l in string:
    print 'This is ' + l
    if l in alpha:
        print (alpha.index(l) + 1)
        print (alpha.index(l) + 1) % 26
        new_l = alpha[(alpha.index(l) + 1) % 26]
        print 'New char is ' + new_l

        print "______________________"
        #newstr += new_l
    elif l in alphaU:
        new_l = alphaU[(alphaU.index(l) + 1) % 25]
        print 'Second line ' + new_l#newstr += new_l
    else:
        print 'Third line ' + new_l
        #newstr += l



##
##newstr2 = ""
##
##for l in newstr:
##    if l in vow:
##        newstr2 += l.upper()
##    else:
##        newstr2 += l
##
##return newstr2

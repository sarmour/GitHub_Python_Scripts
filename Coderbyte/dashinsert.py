string = "99946"
vals=[]
for val in string:
    vals.append(int(val))
newstr = str(string)[0]
for val in range(1,len(vals)):
    if (int(vals[val]) %2 <> 0) and (int(vals[val-1]) %2 <> 0):
        newstr += "-" + str(vals[val])
    else:
        newstr += str(vals[val])
print newstr

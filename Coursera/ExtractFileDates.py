filepath = "C:\users\sarmour\Desktop\mbox-short.txt"
handle = open(filepath)

lst = list()
for line in handle:
    if line.startswith("From "):
        vals = line.split()
        time = vals[5]
        time.split(":")
        hour = time.split(":")[0]
        lst.append(hour)
count = dict()
for val in lst:
    count[val] = count.get(val, 0) + 1
lst2 = sorted([(k,v) for k,v in count.items()])

for k, v in lst2:
    print k, v

##lst2 = dict()
##for vals in lst:
##    lst2[vals] = lst2.get(vals,0) + 1
##
##lst3 = list()
##for key, val in lst2:
##    lst3.append((val, str(key)))
##print lst3
##lst3.sort(reverse= True)
##
##
##for val, key in lst3:
##    print key, val
##handle.close()

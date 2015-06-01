##from collections import Counter
##
##z = ['blue','white','yellow','yellow','red','blue','yellow','red','yellow']
##
##
##Mylist = Counter(z)
##print Mylist
##sorted(Mylist.items(), key=lambda x: x[1])
##
##    
##

string =  "aabb bbcc"
mylist = string.split()
greatest = None
greatest_count = 1

for item in mylist:
    counts = {}
    for ch in item:
        if not ch in counts:
            counts[ch]= 0
        counts[ch] += 1
        count = max(counts.values())
        if count > greatest_count:
            greatest = item
            greatest_count = count
    print counts
print greatest
print greatest_count


##
##def LetterCountI(str): 
##  words = str.split()
##  greatest = None
##  greatest_count = 1
##  for word in words:
##    counts = {}
##    for ch in word:
##      if not ch in counts:
##        counts[ch] = 0
##      counts[ch] += 1
##    count = max(counts.values())
##    if count > greatest_count:
##      greatest = word
##      greatest_count = count
##  
##  return greatest or -1
##    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
    

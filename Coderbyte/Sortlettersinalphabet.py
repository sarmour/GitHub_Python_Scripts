word = 'hello'

mylist = []
for letter in word:
    mylist.append(letter)

print mylist
mylist.sort()
print mylist

print "".join(mylist)

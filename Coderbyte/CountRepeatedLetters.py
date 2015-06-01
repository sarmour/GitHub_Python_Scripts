string = "This is a aabb 1212121212 ttesst"

mylist = string.split()

largestword = None
largestcount = 1

for word in mylist:
    print word
    chars = {}
    for w in word:
        if w not in chars:
            chars[w] = 0
        chars[w] += 1
        count = max(chars.values())
        if count > largestcount:
            largestword = word
            largestcount = count
    if largestword = None
        return "-1"
    else:
        return largestword



def LetterCountI(string): 
	word = string.split()
	lgword = None
	lgcount = 1
    
	for w in word:
		charlist = {}
		for l in w:
			if l in charlist:
				charlist[l] += 1
			else:
				charlist[l] = 1
			count = max(charlist.values())
			if count > lgcount:
				lgword = w
				lgcount = count             
	return lgword or - 1
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCountI(raw_input())  
















  

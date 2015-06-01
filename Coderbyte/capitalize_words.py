words= "hello how are you"
wordlist = words.split()
newword = []
newsentence = []
for word in wordlist:
    word = str(word)
    newfirst = word.upper()[0]
    newrest = word[1:]
    newword = str(newfirst+newrest)
    newsentence.append(newword)
print (' '.join(newsentence)).strip()

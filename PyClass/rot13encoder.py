words = "hahahah"

def str_converted(sen):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    uppers = alph.upper()
    newword = []
    for l in str(sen):
        if l in alph:
            newword.append(alph[(alph.index(l)+13)%26])
        elif l in uppers:
            newword.append(uppers[(uppers.index(l)+13)%26])
        else:
            newword.append(l)
    return "".join(newword)

print str_converted(words)

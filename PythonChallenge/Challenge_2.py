""" Challenge 2 clue: Recognize the characters. maybe they are in the book, but MAYBE they are in the page source.

    http://www.pythonchallenge.com/pc/def/ocr.html

    I viewed the page source and found a long text string. Returning second part of that string.
"""

import urllib2

vals = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()
newvals = vals.split("<!--\nfind rare characters in the mess below:\n-->\n\n<!--")[1]
charcounter = {}

for l in newvals:
    charcounter[l] = charcounter.get(l,0) + 1

print charcounter

###here is the character count.
# {6079, '#': 6115, '%': 6104, '$': 6046, '&': 6043, ')': 6186, '(': 6154, '+': 6066, '*': 6034, '-': 2, '>': 1, '@': 6157, '[': 6108, ']': 6152, '_': 6112, '^': 6030, 'a': 1, 'e': 1, 'i': 1, 'l': 1, 'q': 1, 'u': 1, 't': 1, 'y': 1, '{': 6046, '}': 6105}

### need to figure out what this spells
# a, e, i, l, q, u, t, y

###answer
# equality

import urllib2

vals = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

newvals = vals.split("<!--\n")[1].replace('\n','')[:-3] #extract the source page challenge text
print newvals
answer = ''

for i, l in enumerate(newvals):
    #using try and except to skip first and last index issues
    try:
        if newvals[i].islower() and newvals[i-3:i].isupper() and newvals[i-4].islower() and newvals[i+1:i+4].isupper() and newvals[i+4].islower():
            answer += l
    except:
        continue
print answer




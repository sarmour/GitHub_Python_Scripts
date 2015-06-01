

##def LetterChanges(string): 
##    text = str(string)
##    newword = ""
##    chars = []
##    alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,y,x,z'
##    chars = alphabet.split(',')
##
##    for letter in text:
##        if letter.isspace():
##            newword += " "
##        else:
##            for i in range(len(chars)):
##                if letter == chars[i]:
##                    newword += chars[i+1]
##    vowels = ['a','e','i','o','u']
##    newestword = ""
##    for l in newword:
##        
##        if l in vowels:
##            newestword += l.upper()
##        else:
##            newestword +=l
##    return newestword
##
##print LetterChanges(raw_input())

###############someone else's code############################
##
##def LetterChanges(str): 
####should be 26 below
##  alpha = "abcdefghijklmnopqrstuvwxyz"
##  alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##  vow = "aeiouAEIOU"
##  
##  newstr = ""
##  
##  for l in str:
##    if l in alpha:
##      new_l = alpha[(alpha.index(l) + 1) % 25]
##      newstr += new_l
##    elif l in alphaU:
##      new_l = alphaU[(alphaU.index(l) + 1) % 25]
##      newstr += new_l
##    else:
##      newstr += l
##  
##  newstr2 = ""
##  
##  for l in newstr:
##    if l in vow:
##      newstr2 += l.upper()
##    else:
##      newstr2 += l
##  
##  return newstr2
##  
##    
### keep this function call here  
### to see how to enter arguments in Python scroll down
##print LetterChanges(raw_input())         

str = 'zZ!!'
undercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowel = 'AEIOUaeiou'
newstr = ''

for l in str:
    print l
    if l in undercase:
        newstr += undercase[(undercase.index(l)+1)%26]
    elif l in uppercase:
        newstr += uppercase[(uppercase.index(l)+1)%26]
    else:
        newstr += l
print newstr
newstr2 = ''
for v in newstr:
    if v in vowel:
        newstr2 += v.upper()
    else:
        newstr2 += v
print newstr2

string = "Which of these wordddddddddddddddddds is the longest"

total = []

for val in string.split():
    total.append(val)
print total
total.sort(key =len, reverse = True)
print total

###This code is better
##def LongestWord(sen): 
##  inc = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
##  sen = ''.join([ch for ch in sen if ch in inc])
##  largest = ''
##  largest_size = 0
##  words = sen.split()
##  for word in words:
##    if len(word) > largest_size:
##       largest = word
##       largest_size = len(word)
##  return largest
##    
##    
### keep this function call here  
### to see how to enter arguments in Python scroll down
##print LongestWord(raw_input())           

def FirstReverse(string): 

  vals = ''
  words = str(string)
  for letter in range(len(words),0,-1):
   	vals += words[letter-1]
  return vals
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input())  

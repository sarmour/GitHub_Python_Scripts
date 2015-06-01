##numbers = "0123456789"
##
##def NumberAddition(str): 
##  result = 0
##  for l in str:
##    if l not in numbers:
##      str = str.replace(l,' ')
##  vals= str.split()
##  for val in vals:
##    result+= int(val)
##  return result
##print NumberAddition("75NumberN9")  
##
##
##
##
##
##
##






def NumberAddition(str): 
  sum = 0
  coeff = 0
  for ch in str:
    if ch.isdigit():
      coeff = 10 * coeff + int(ch)
    else:
      sum += coeff
      coeff = 0
  sum = coeff
      
  return sum
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print NumberAddition("75Number9")           





  

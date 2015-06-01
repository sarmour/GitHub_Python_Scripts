##num = 100
##
##def PrimeNumber(num):
##
##    prime = True
##
##    for i in range(2,num)[::-1]:
##        if num% i == 0:
##            prime = False
##            return prime
##    return prime
##
##def PrimeMover(num): 
##  go = True
##  i = 2
##  prm = 0
##
##  while go:
##    print i, prm
##    if PrimeNumber(i):
##        prm +=1
##    if prm == num:
##      return i
##    i += 1
##
### keep this function call here  
### to see how to enter arguments in Python scroll down
##print PrimeMover(num)  
##
##
##
##
##
##
##

num = 100
def PrimeMover(num): 
  go = True
  i = 2
  prm = 0
 
  while go:
    print i, num
    prime = "true"
    
    for v in range(2,i):
      if i%v == 0:
        prime = "false"
        
    if prime <> "false":
    	prm +=1
    if prm == num:
      return i
    i += 1

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeMover(num)  
















  







  

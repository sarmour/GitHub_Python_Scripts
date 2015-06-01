myarray = [1,3,5,10,2,5]
myarray.sort()
##answer = 'false'
##for i in range(len(myarray)):
##    val = 0
##    for ct in range(len(myarray)):
##        val += myarray[ct]
##        if val == myarray[i]:
##            print myarray[ct]
##            print myarray[i]
##            print val
##            answer = 'true'
####        if myarray[i-1] + myarray[i-2] == myarray[i]:
####            answer = 'true'
##        
##print answer
def ArrayAdditionI(myarray): 

  from itertools import combinations
  answer = "false"
  for i in range(2,len(myarray)+1):
      vals = combinations(myarray,i)
      for val in vals:
          if max(myarray) == sum(val):
              answer = "true"
  return answer
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArrayAdditionI(raw_input())  

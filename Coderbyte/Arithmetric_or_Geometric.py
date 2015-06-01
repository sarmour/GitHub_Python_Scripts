nums= [5,10,15]
##nums = [2,4,16,24]

def ArithGeo(arr): 
    i = 1
    firstdif = 0.0
    firstratio = 0.0


    firstdif = float(arr[1]) - arr[0]
    while float(arr[i]) - arr[i-1] ==  firstdif:
        i +=1
        if i == len(arr):
            return "Arithmetic"

    firstratio = float(arr[1])/arr[0]
    while float(arr[i])/arr[i-1] ==  firstdif:
        i +=1
        if i == len(arr):
            return "Geometric"

    return -1
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeo(nums)  


Someoneelses
##
##
##
##def ArithGeo(arr): 
##  if len(arr) < 2:
##    return -1
##  a = arr[1] - arr[0]
##  g = arr[1] / arr[0]
##  
##  isA = True
##  isG = True
##  
##  prev = arr[1]
##  for n in arr[2:]:
##    if n != prev + a:
##      isA = False
##    if n != prev * g:
##      isG = False
##    prev = n
##      
##  if isA:
##    return 'Arithmetic'
##  elif isG:
##    return 'Geometric'
##  else:
##    return -1
##    
##    
### keep this function call here  
### to see how to enter arguments in Python scroll down
##print ArithGeo(raw_input())           

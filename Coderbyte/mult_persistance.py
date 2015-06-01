num = 39

def mult_persistance(val):
    count = 0
    while len(str(val)) > 1:

        strval = str(val)
        nums = []

        for n in strval:
            nums.append(int(n))
        val = reduce(lambda x, y: x*y, nums)
        count += 1
    return count
        
    
print mult_persistance(num)
##
##def MultiplicativePersistence(num): 
##    count = 0
##    while len(str(num))>1:
##        nums = []
##        for l in str(num):
##            nums.append(int(l))
##        
##        num = 1
##        for n in nums:
##          num *=n
##        count += 1
##    return count
##    
##    
### keep this function call here  
### to see how to enter arguments in Python scroll down
##print MultiplicativePersistence(raw_input())  

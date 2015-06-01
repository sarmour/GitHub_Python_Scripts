num = 2718

def additive_persistance(val):
    count = 0
    while len(str(val)) > 1:

        strval = str(val)
        nums = []

        for n in strval:
            nums.append(int(n))
        val = sum(nums)
        count += 1
    return count
        
    
print additive_persistance(num)

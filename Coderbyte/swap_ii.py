##"""Using the Python language, have the function SwapII(str)
##take the str parameter and swap the case of each character.
##Then, if a letter is between two numbers (without separation),
##switch the places of the two numbers. \
##For example: if str is "6Hello4 -8World, 7 yes3"
##the output should be 4hELLO6 -8wORLD, 7 YES3"
##


def SwapII(str): 

    new = str.swapcase()

    newword = ''
    newsentence = []
    count = 0

    for word in new.split():
        count = 0
        for l in word:
            if l.isdigit():
                count +=1
        if count >= 2:
            nums = []
            ind = []
            i = 0
            for l in word:
                if l.isdigit():
                    nums.append(l)
                    ind.append(i)
                i +=1 
            zipped = zip(nums,ind)
            print v, i 



print SwapII("6Hello4 -8World, 7 yes3")  











##        ct = 0
##        nums = []
##        for l in word:
##            if l.isdigit():
##                ct += 1
##                nums.append(l)
##        
##        if ct>=2():
##            i = 0
##            for l in word:
##                tmp.append(l)
##
##            startpos = l.index(nums[o])
##            endpos = l.index(nums[1])
##
####            for l in word:
####                if l in nums:
####                    
####                
####        newword = "".join(lst)
####                
##        if newword <> "": newsentence.append(newword)
##        else: newsentence.append(word)
##        newword = ''
##    return " ".join(newsentence)
# keep this function call here  
# to see how to enter arguments in Python scroll down
















  

str1 = "cdore"
str2 = "coder"

def StringScramble(str1,str2): 
    mylst =[]
    match = True
    for i in str1:
        mylst.append(i)

    for i in str2:
        if i in mylst:
            match = True
            mylst.remove(i)
        else:
            match = False
    return match
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble(str1,str2)  



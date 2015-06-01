words = "Noel - sees Leon"
def PalindromeTwo(sens): 
    newword = ''
    for val in sens:
        if val.isalpha():
            newword+=val.lower()
    if newword == newword[::-1]:
        return True
    else:
        return False

# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo(words)  
















  

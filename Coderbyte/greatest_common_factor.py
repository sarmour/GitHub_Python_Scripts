num1 = 36
num2 = 54
def common_factors(num1, num2):
    go = True
    i = max(num1, num2)
    while go == True:
        if num1%i ==0 and num2%i==0 and num1 >=i and num2>= i:
            go == False
            return i
        
        i -= 1
        

print common_factors(num1, num2)
    

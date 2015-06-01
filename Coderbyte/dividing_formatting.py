def DivisionStringified(num1,num2): 
	num1 = float(num1)
	num2 = float(num2)
	num3 = round(num1/num2,0)
	return "{:,}".format(int(num3))
    
print DivisionStringified(raw_input())  

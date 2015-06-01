##mylist = range(11)
##print mylist
##
##binaries = dict([])
##
##for item in mylist:
##    binaries[item] = bin(item)
##
##for item in binaries:
##    print int(binaries[item],2)
####print max(binaries.values())
####print binaries.key("0b111")


def BinaryConverter(string): 

	value = int(string,2)
	return value
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print BinaryConverter(raw_input())  

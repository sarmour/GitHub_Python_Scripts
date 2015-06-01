import numpy as np

##a = np.array((1,2,3,4), float)
####print a 
##
a = np.array(((1,2,3,4),(5,6,7,8)), float)
####print a [0,1]
####print a [1,1]
##
####print a[1:] ##inclusive
##
####print a[:1] ##exlusive 
##
####print a[-1:,-2:] ##need to figure out how this works
##
##print a.shape
##print a.dtype
##
##print 2 in a
##print 10 in a

#a = np.array(range(10), float) #range is not inclusive

##print a
##
##a= a.reshape(5,2)
##print a
##
##b = a
##c = a.copy() #this will copy the original a and not the updates. its called name binding. 
##
##a[0] = 5
##print a
##print b
##print c 

#a.append("text") #this will fail
##a=  a.tolist()
##a.append("text") #this will work because its a list now. 
##print a

##s= a.tostring() #this didnt work properly. Not showing correct values. Can help store large amounts of data in files that can be read later
##print s
##s= np.fromstring(s)
##print s
print a
print a.transpose() #didnt work

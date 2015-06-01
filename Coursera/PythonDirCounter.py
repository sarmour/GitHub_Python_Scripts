##import os
##
##for fl in os.listdir("C:\users\sarmour\desktop"):
##    print fl

name = "c:\users\sarmour\desktop\mbox-short.txt"

fa = open(name,"r")

senders = {}
for row in fa:
    if row.startswith("From "):
        sender = row.split()[1]
        senders[sender] = senders.get(sender,0) + 1
        
bigsender = None
bigvalue = None


for sender,val in senders.items():
    if val is None or val > bigvalue:
        bigsender = sender
        bigvalue = val

print bigsender, bigvalue
    

fa.close()        

string = "12:30pm-12:00am"
vals = string.split("-")

time1= str(vals[0])
time2= str(vals[1])

total1 = 0
total2 = 0
difference =0

if time1[-2:] == "pm" and time1[2:] <> "12":
    hour1 = 12
elif time1[-2:] == "am" and time1[2:] <> "12":
    hour1 = 24
else:
    hour1 = time1[2:]
    
min1 = int(str(time1.split(":")[1])[:2])
total1 = int(hour1 * 60) + int(min1)

if time2[-2:] == "pm" and time2[2:] <> "12":
    hour2 = 12
elif time2[-2:] == "am" and time2[2:] <> "12":
    hour2 = 24
else:
    hour2 = time2[2:]

min2 = int(str(time2.split(":")[1])[:2])
total2 = int(hour2 * 60) + int(min2)



if total1 > total2:
    difference = (total2+1440- total1)
else:
    difference = total2- total1

print difference



##def CountingMinutesI(str): 
##  strs = str.split('-')
##  comps1 = strs[0].split(':')
##  min1 = int(comps1[0]) * 60 + int(comps1[1][:2])
##  des1 = comps1[1][2:4]
##  comps2 = strs[1].split(':')
##  min2 = int(comps2[0]) * 60 + int(comps2[1][:2])
##  des2 = comps2[1][2:4]
##  
##  diff = min2 - min1
##  if des1 != des2:
##    diff += 12 * 60
##  elif min1 >= min2:
##    diff += 24 * 60
##
##  return diff
##    
##    
### keep this function call here  
### to see how to enter arguments in Python scroll down
##print CountingMinutesI(raw_input())           

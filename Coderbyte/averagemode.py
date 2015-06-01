vals = [1,2,3,3,4,5,6]

average = sum(vals)/float(len(vals))
print average

ct = 0
count = {}
for val in vals:
    if val not in count:
        count[val] = 0
    count[val]+=1
    if count[val] > ct:
        ct = count[val]
        mode = str(val)
print max(count.values())
print mode


def MeanMode(vals): 
  vals.sort()
  average = int(round(sum(vals)/float(len(vals)),0))
  ct = 0
  count = {}
  for val in vals:
      if val not in count:
          count[val] = 0
      count[val]+=1
      if count[val] > ct:
          ct = count[val]
          mode = str(val)
  if int(mode) == int(average):
  	return 1
  else:
    return 0
  
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MeanMode(raw_input())  

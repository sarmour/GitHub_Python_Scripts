string = "Laura sobs"

answer = 'false'

for i in range(len(string)):
    print i
    print string[i]
    if string[i] == 'a' and string[i+4] =='b':
        answer = 'true'
print answer



def ABCheck(string):

  string = string.lower()

  status = "false"

  for n in range(0, len(string)):
    if string[n] == "a":
      try:
        if string[n-4] == "b":
          status = "true"
      except:
          continue
      try:
        if string[n+4] == "b":
          status = "true"
      except:
          continue

  return status

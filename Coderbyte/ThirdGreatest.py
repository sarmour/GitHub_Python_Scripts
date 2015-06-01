test = ["coder","byte","code"]

def ThirdGreatest(strArr): 

  lens = []

  for word in test:
      lens.append(len(word))
  comb = zip(test,lens)
  print sorted(comb,key=lambda x: x[1], reverse= True) [2] [0]
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThirdGreatest(test)  
















  

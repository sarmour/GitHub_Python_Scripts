lst = ["4","E","1","E","2","E","3","E"]
lst = ["1","2","E","E","3"]
def OffLineMinimum(lst): 
    nums = []
    newlst = []
    for l in lst:
        if l.isdigit():
           nums.append(int(l))
        if l == "E":
            newlst.append(str(min(nums)))
            nums.remove(min(nums))
    final = ",".join(newlst)
    return final
# keep this function call here  
# to see how to enter arguments in Python scroll down
print OffLineMinimum(lst)  

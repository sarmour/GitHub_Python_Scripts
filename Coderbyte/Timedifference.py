time1 = "12:45"
time2 = "13:30"

hours1 = time1.split(":")[0]
minutes1 = time1.split(":")[1]
hours2 = time2.split(":")[0]
minutes2 = time2.split(":")[1]

totaltime1 = (int(hours1) *60) + int(minutes1)
totaltime2 = (int(hours2) *60) + int(minutes2)

newtime = totaltime2 - totaltime1

hours = int(newtime/60)
minutes = newtime - (hours * 60)

print str(hours) + ":" + str(minutes)


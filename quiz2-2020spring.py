basicInfo = (input()).split(",")
export = (input()).split(",")
for i in range(len(basicInfo)):
    basicInfo[i] = eval(basicInfo[i])
for i in range(len(export)):
    export[i] = eval(export[i])
stock = basicInfo[0]
requiredDays = basicInfo[1]
Import = basicInfo[2]
importTimes = basicInfo[3]
day = 1
count = 0
left = stock
exportDays = []
while count < importTimes:
    index = (day - 1) % 7
    left -= export[index]
    if left < export[(index+1) % 7]:
        exportDays.append(day-requiredDays + 1)
        left += Import
        count += 1
        day += 1
    else:
        day += 1
for i in range(len(exportDays)):
    exportDays[i] = str(exportDays[i])
print(",".join(exportDays))

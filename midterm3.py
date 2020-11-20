data1 = input().split(",")
data2 = input().split(",")
amount = eval(data1[0])
limit = eval(data1[1])
for i in range(len(data2)):
    data2[i] = eval(data2[i])
data2.sort(reverse=True)
boxInfo = [limit]
for item in data2:
    Return = ""
    for i in range(len(boxInfo)):
        if item <= boxInfo[i]:
            boxInfo[i] -= item
            Return = "OK"
            break
    if Return != "OK":
        boxInfo.append(limit)
        boxInfo[-1] -= item
print(len(boxInfo))

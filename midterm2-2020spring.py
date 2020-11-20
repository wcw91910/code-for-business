data1 = input().split(",")
data2 = input().split(",")
upperLimit = int(data1[2])
lowerLimit = int(data1[1])
for i in range(len(data2)):
    data2[i] = eval(data2[i])
count = 0
for num in data2:
    if num <= upperLimit and num >= lowerLimit:
        count += 1
print(count)

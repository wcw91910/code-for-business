data1 = input().split(",")
data2 = input().split(",")
data3 = input().split(",")
amount = int(data1[0])
budget = int(data1[1])
risk = int(data1[2])
alreadyBought = []
haventBought = []
price = []
exp = []
for i in range(amount):
    price.append(int(data2[i]))
    exp.append(int(data3[i]))
var = []
for i in range(amount):
    data4 = input().split(",")
    for j in range(len(data4)):
        data4[j] = int(data4[j])
    var.append(data4)
for i in range(amount):
    haventBought.append(i)
# 尋找最大目標值
while True:
    targetVaule = []
    for i in haventBought:
        vaule = exp[i] - risk*var[i][i]
        for x in alreadyBought:
            vaule -= 2*risk*var[i][x]
        if vaule > 0 and (budget - price[i]) >= 0:
            targetVaule.append([1 / vaule, price[i], i])  # 運用倒數技巧排序
    if len(targetVaule) > 0:
        targetVaule.sort()
        largestIndex = targetVaule[0][2]
        budget -= price[largestIndex]
        alreadyBought.append(largestIndex)
        haventBought.remove(largestIndex)
        if len(haventBought) == 0:
            alreadyBought.sort()
            for i in range(len(alreadyBought)):
                alreadyBought[i] = str(alreadyBought[i] + 1)
            print(",".join(alreadyBought))
            break
    else:
        if len(alreadyBought) == 0:
            print(0)
            break
        else:
            alreadyBought.sort()
            for i in range(len(alreadyBought)):
                alreadyBought[i] = str(alreadyBought[i] + 1)
            print(",".join(alreadyBought))
            break

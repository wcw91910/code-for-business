data1 = input().split(",")
weight = input().split(",")
utility = input().split(",")
amount = int(data1[0])
weightLimit = int(data1[1])
buyedItems = []
# 先轉換為int型態
for i in range(len(weight)):
    weight[i] = int(weight[i])
for i in range(len(utility)):
    utility[i] = int(utility[i])
# 計算CP值
originalCP = []
for i in range(len(weight)):
    CPVaule = utility[i] / weight[i]
    originalCP.append(CPVaule)
sortedCP = []
for i in range(len(originalCP)):
    sortedCP.append(originalCP[i])
sortedCP.sort()
sortedCP.reverse()
# 放入東西
totalWeight = 0
for i in range(len(weight)):
    totalWeight += weight[originalCP.index(sortedCP[i])]
    if totalWeight <= weightLimit:
        buyedItems.append(originalCP.index(sortedCP[i]) + 1)
    else:
        totalWeight -= weight[originalCP.index(sortedCP[i])]
buyedItems.sort()
for i in range(len(buyedItems)):
    buyedItems[i] = str(buyedItems[i])
print(",".join(buyedItems))

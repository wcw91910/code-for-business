data1 = input().split(",")
weight = input().split(",")
utility = input().split(",")
itemsCondition = input().split(",")
amount = int(data1[0])
weightLimit = int(data1[1])
# 先轉換為int型態
for i in range(len(weight)):
    weight[i] = int(weight[i])
for i in range(len(utility)):
    utility[i] = int(utility[i])
for i in range(len(itemsCondition)):
    itemsCondition[i] = int(itemsCondition[i])
# 計算總重量及效用
totalWeight = 0
totalUtility = 0
for i in range(len(itemsCondition)):
    if itemsCondition[i] == 1:
        totalWeight += weight[i]
        totalUtility += utility[i]
# 計算是否在限制內
if totalWeight <= weightLimit:
    print(totalWeight, totalUtility, sep = ",")
else:
    print(-1)

"""演算法1"""
data1 = input().split(",")
weight = input().split(",")
utility = input().split(",")
amount = int(data1[0])
weightLimit = int(data1[1])
# 先轉換為int型態
for i in range(len(weight)):
    weight[i] = int(weight[i])
for i in range(len(utility)):
    utility[i] = int(utility[i])
# 計算CP值
CPWeightIndex = []
for i in range(len(weight)):
    CPVaule = utility[i] / weight[i]
    CPWeightIndex.append([1 / CPVaule, weight[i], i])  # 利用CP值倒數的技巧做Index的順序排序
CPWeightIndex.sort()
# 計算總效用
totalUtility = 0
totalWeight = 0
buyedItems = []
for i in range(len(CPWeightIndex)):
    currentIndex = CPWeightIndex[i][2]
    totalWeight += weight[currentIndex]
    if totalWeight <= weightLimit:
        totalUtility += utility[currentIndex]
        buyedItems.append(currentIndex + 1)
    else:
        totalWeight -= weight[currentIndex]
result = totalUtility
"""演算法2"""
# 排序utility
sortedUtilityWeightIndex = []
for i in range(len(utility)):
    sortedUtilityWeightIndex.append([1 / utility[i], weight[i], i])  # 同理，利用倒數技巧對index做排序
sortedUtilityWeightIndex.sort()
# 計算總效用
totalUtility2 = 0
totalWeight2 = 0
buyedItems2 = []
for i in range(len(sortedUtilityWeightIndex)):
    currentIndex = sortedUtilityWeightIndex[i][2]
    totalWeight2 += weight[currentIndex]
    if totalWeight2 <= weightLimit:
        totalUtility2 += utility[currentIndex]
        buyedItems2.append(currentIndex + 1)
    else:
        totalWeight2 -= weight[currentIndex]
result2 = totalUtility2
"""比較兩者演算法"""
if result > result2:
    buyedItems.sort()
    for i in range(len(buyedItems)):
        buyedItems[i] = str(buyedItems[i])
    print(",".join(buyedItems))
else:
    buyedItems2.sort()
    for i in range(len(buyedItems2)):
        buyedItems2[i] = str(buyedItems2[i])
    print(",".join(buyedItems2))

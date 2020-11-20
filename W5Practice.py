inPrice = eval(input())
outPrice = eval(input())
demand = eval(input())
salvage = eval(input())
# 取得機率
p = []
for i in range(demand+1):
    p.append(eval(input()))


def countExp():
    expectationVaule = 0
    for i in range(amount):
        expectationVaule += (outPrice*i - inPrice*(supply - i) + salvage*(supply - i))*p[i] # 先算扣掉amount本身以外的期望值
    sum = 0
    for i in range(amount):
        sum += p[i] 
    left = 1 - sum  # amount(含)之後的機率總和
    expectationVaule += (amount*outPrice- inPrice*(supply - amount) + salvage*(supply - amount))*left  # 把amount本身加回去
    return "{:.2f}".format(expectationVaule)


ls = []
for supply in range(demand + 1):
    if demand <= supply:
        amount = demand
    else:
        amount = supply
    ls.append(countExp())
print(ls)
# 把str轉float
for i in range(len(ls)):
    ls[i] = eval(ls[i])
index = 0
largest = ls[0]
for i in range(len(ls)):
    if ls[i] > largest:
        index = i
        largest = ls[i]
    else:
        continue
print(index, int(largest))

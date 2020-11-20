inPrice = eval(input())
outPrice = eval(input())
demand = eval(input())
supply = eval(input())
# 取得機率
p0 = eval(input())
p1 = eval(input())
p2 = eval(input())
p3 = eval(input())
p4 = eval(input())
p5 = eval(input())
p6 = eval(input())
p7 = eval(input())
p8 = eval(input())
# amount取得相對較小值
if demand <= supply:
    amount = demand
else:
    amount = supply
ls = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
expectationVaule = 0
for i in range(amount):
    expectationVaule += i*ls[i]  # 先算扣掉amount本身以外的期望值
sum = 0
for i in range(amount):
    sum += ls[i]
left = 1 - sum  # amount(含)之後的機率總和
expectationVaule += amount*left  # 把amount本身加回去
income = outPrice*expectationVaule-inPrice*supply
income = int(income)  # 進行無條件捨去
print(income)

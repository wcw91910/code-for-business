num = int(input())
index = (input()).split(",")
price = (input()).split(",")
amount = (input()).split(",")
# 先轉成數字型態
for i in range(len(index)):
    index[i] = int(index[i])
for i in range(len(price)):
    price[i] = int(price[i])
    amount[i] = int(amount[i])
# 先存儲全部不折扣的價錢
oriTotal = 0
for i in range(len(price)):
    oriTotal += price[i]*amount[i]
# 湊5組的
dividedBy5 = []
for i in index:
    dividedBy5.append(amount[i-1]//5)
dividedBy5.sort()
packOf5 = dividedBy5[0]
for i in index:
    amount[i-1] -= packOf5*5  # 扣掉已成5組的
# 湊1組的
dividedBy1 = []
for i in index:
    dividedBy1.append(amount[i-1]//1)
dividedBy1.sort()
packOf1 = dividedBy1[0]
for i in index:
    amount[i-1] -= packOf1  # 扣掉已成1組的
# 算剩下沒折扣的價錢
total = 0
for i in range(len(price)):
    total += price[i]*amount[i]
# 加上有折扣的價錢
for i in index:
    total += (5*packOf5*0.8 + packOf1*0.9)*price[i-1]
save = oriTotal - total
newStudents = save//1000
if newStudents <= 0:
    print("So sad. I messed up.")
else:
    print(int(total), int(newStudents), sep=",")

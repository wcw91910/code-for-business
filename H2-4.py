sleepDay = int(input())
sleepHour = []
for i in range(sleepDay):
    sleepHour.append(float(input()))
lemonAmount = 0
sugarAmount = 0
proteinAmount = 0
for i in range(len(sleepHour)):
    if sleepHour[i] > 7:
        lemonAmount += 1
# 計算平均
sum = 0
for i in range(len(sleepHour)):
    sum += sleepHour[i]
    avr = sum/len(sleepHour)
if avr <= 6:
    sugarAmount = sleepDay - lemonAmount
else:
    proteinAmount = sleepDay - lemonAmount
# 計算材料數量
lemonFruit = 1.5*lemonAmount
almond = 4*lemonAmount + 9*sugarAmount
honey = 18*sugarAmount + 6*proteinAmount
egg = 2*proteinAmount
totalPrice = 0
# 計算 lemonFruit 價錢
if lemonFruit - lemonFruit//1 != 0:
    lemonFruit = lemonFruit//1 + 1
if lemonFruit >= 5:
    totalPrice += 7*lemonFruit*0.9
else:
    totalPrice += 7*lemonFruit
# 計算 almond 價錢
totalPrice += 0.6*almond
# 計算 honey 價錢
totalPrice += 1.2*honey
# 計算 egg 價錢
if egg/3 - egg//3 != 0:
    totalPrice += 25*(egg//3 + 1)
else:
    totalPrice += 25*(egg//3)
print(int(totalPrice))

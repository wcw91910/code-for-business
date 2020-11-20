data1 = input()
amountAndLeastBuy = data1.split(",")
data2 = input()
sepAndSepPrice = data2.split(",")
amount = int(amountAndLeastBuy[0])
leastBuy = int(amountAndLeastBuy[1])
sepVaule = leastBuy
# 把list中元素轉為int
for i in range(len(sepAndSepPrice)):
    sepAndSepPrice[i] = int(sepAndSepPrice[i])
sep = []
sepPrice = []
for i in range(amount):
    sep.append(sepAndSepPrice[i])
for i in range(amount, amount*2):
    sepPrice.append(sepAndSepPrice[i])
total = 0
# 算剛好買完價錢
for i in range(amount):
    if i == 0:
        left = leastBuy
        if left > sep[i]:
            total += sep[i]*sepPrice[i]
        else:
            total += left*sepPrice[i]
            count = i
            break
    else:
        left = leastBuy
        left -= sep[i-1]
        if left > (sep[i]-sep[i-1]):
            accumulate = sep[i-1]
            total += (sep[i]-accumulate)*sepPrice[i]
        else:
            total += left*sepPrice[i]
            count = i
            break
# 算下面級距買完價錢
while count < len(sep):
    newTotal = 0
    for i in range(count + 1):
        if i == 0:
            left = sep[count]
            if left > sep[i]:
                newTotal += sep[i]*sepPrice[i]
            else:
                newTotal += left*sepPrice[i]
                break
        else:
            left = sep[count]
            left -= sep[i-1]
            if left > (sep[i]-sep[i-1]):
                accumulate = sep[i-1]
                newTotal += (sep[i]-accumulate)*sepPrice[i]
            else:
                newTotal += left*sepPrice[i]
                break
    if newTotal <= total:
        total = newTotal
        sepVaule = sep[count]
    count += 1
print(sepVaule, total, sep=",")

data1 = input()
amountAndLeastBuy = data1.split(",")
data2 = input()
sepAndSepPrice = data2.split(",")
amount = int(amountAndLeastBuy[0])
leastBuy = int(amountAndLeastBuy[1])
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
accumulate = 0
for i in range(amount):
    if i == 0:
        left = leastBuy
        if left > sep[i]:
            total += sep[i]*sepPrice[i]
        else:
            total += left*sepPrice[i]
            break
    else:
        left = leastBuy
        left -= sep[i-1]
        if left > (sep[i]-sep[i-1]):
            accumulate = sep[i-1]
            total += (sep[i]-accumulate)*sepPrice[i]
        else:
            total += left*sepPrice[i]
            break
print(total)

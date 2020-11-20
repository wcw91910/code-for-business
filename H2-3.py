amount = int(input())
leastBuy = int(input())
sep = []
sepPrice = []
for i in range(amount):
    sep.append(int(input()))
    sepPrice.append(int(input()))
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

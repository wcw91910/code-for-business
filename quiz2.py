data1 = input().split(",")
data2 = input().split(",")
price1 = eval(data1[0])
price2 = eval(data1[1])
discount = eval(data1[2])
amount = eval(data1[3])
for i in range(len(data2)):
    data2[i] = eval(data2[i])
box = 0
drink = 0
box += data2.count(1)
box += data2.count(3)
drink += data2.count(2)
drink += data2.count(3)
discountPrice = price1 + price2 - discount
if discountPrice <0:
    discountPrice = 0
total = price1*data2.count(1) + price2*data2.count(2) + discountPrice*data2.count(3)
if total < 0:
    total = 0
ls = []
ls.append(box)
ls.append(drink)
ls.append(total)
for i in range(len(ls)):
    ls[i] = str(ls[i])
print(",".join(ls))

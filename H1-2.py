full = int(input())
fullPrice = int(input())
student = int(input())
studentPrice = int(input())
pay = int(input())
maxium = int(input())
total = full*fullPrice + student*studentPrice
left = maxium - full - student
if (full + student) > maxium:
    print("-1", end=",")
else:
    print(left, end=",")
if pay < total:
    print("-2")
else:
    print("${}".format(pay - total))

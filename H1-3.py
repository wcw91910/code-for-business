full = int(input())
fullPrice = int(input())
student = int(input())
studentPrice = int(input())
pay = int(input())
maxium = int(input())
total = full*fullPrice + student*studentPrice
left = maxium - full - student
if (full + student) <= maxium:
    print(left, end=",")
if pay >= total:
    print("${}".format(pay - total))

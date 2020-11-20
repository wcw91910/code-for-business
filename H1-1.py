full = int(input())
fullPrice = int(input())
student = int(input())
studentPrice = int(input())
pay = int(input())
total = full*fullPrice + student*studentPrice
if pay < total:
    print("-1")
else:
    print("${}".format(pay - total))

x1=eval(input())
x2=eval(input())
fullPrice=eval(input())
studentPrice=eval(input())
pay=eval(input())
amount=x1*fullPrice+x2*studentPrice
change=pay-amount
print(pay, amount, change, sep=",")
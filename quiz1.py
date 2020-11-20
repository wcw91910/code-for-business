price1 = eval(input())
price2 = eval(input())
discount = eval(input())
total = price1 + price2 - discount
if total >= 0 :
    print(total)
else:
    print(0)

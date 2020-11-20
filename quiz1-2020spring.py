num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
if num1 + num2 == num3 or num1 + num3 == num2 or num2 + num3 == num1:
    print(1)
else:
    print(0)
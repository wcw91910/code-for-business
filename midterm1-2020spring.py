num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
ls1 = [num1, num2, num3]
ls2 = [num1, num3, num4]
ls3 = [num1, num2, num4]
ls4 = [num2, num3, num4] 
ls1.sort()
ls2.sort()
ls3.sort()
ls4.sort()
# print(ls1, ls2, ls3, ls4)
count = 0
if ls1[0] + ls1[1] == ls1[2]:
    count += 1
if ls2[0] + ls2[1] == ls2[2]:
    count += 1
if ls3[0] + ls3[1] == ls3[2]:
    count += 1
if ls4[0] + ls4[1] == ls4[2]:
    count += 1
print(count)
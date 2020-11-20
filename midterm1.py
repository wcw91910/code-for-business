num1 = int(input())
num2 = int(input())
data = num1 - num2
ls = [0]
ls.append(data)
ls.sort(reverse=True)
print(ls[0])

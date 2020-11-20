amount = eval(input())
numbers = input().split(",")
for i in range(len(numbers)):
    numbers[i] = eval(numbers[i])
# 相減並存入ls
ls = []
for i in range(len(numbers) - 1):
    data = numbers[i] - numbers[i + 1]
    if data >= 0:
        ls.append(data)
    else:
        ls.append(0)
print(min(ls))

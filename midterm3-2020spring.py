amount = eval(input())
x = input().split(",")
y = input().split(",")
for i in range(amount):
    x[i] = eval(x[i])
    y[i] = eval(y[i])
ls = []
for i in range(len(x)):
    distance = []
    for j in range(len(y)):
        distance.append(abs(x[j] - x[i])+abs(y[j] - y[i]))
    ls.append(distance)
for i in range(len(ls)):
    for j in range(len(ls)):
        ls[i][j] = str(ls[i][j])
for i in range(len(ls)):
    print(",".join(ls[i]), sep="\n")

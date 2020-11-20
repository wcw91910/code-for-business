amount, maximum = eval(input())
getOff = input().split(",")
getIn = input().split(",")
for i in range(amount):
    getOff[i] = eval(getOff[i])
    getIn[i] = eval(getIn[i])

code = []
currentPpl = 0
currentStation = 0
while currentStation < amount:
    currentPpl -= getOff[currentStation]
    if currentPpl < 0:
        code.append(1)
    elif currentPpl > maximum:
        code.append(2)
    else:
        code.append(0)
    currentPpl += getIn[currentStation]
    if currentPpl < 0:
        code.append(1)
    elif currentPpl > maximum:
        code.append(2)
    else:
        code.append(0)
    currentStation += 1
# print(code)
if 1 not in code and 2 not in code:
    print("{},{}".format(currentPpl, 0))
else:
    while 0 in code:
        code.remove(0)
    print("{},{}".format(currentPpl, code[0]))
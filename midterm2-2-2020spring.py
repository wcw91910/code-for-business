# def main():
#     getOff, getIn, amount, maximum = getData()
#     people, code = run(getOff, getIn, 0, 0)
#     outPut(code, people)

# def getData():
#     amount, maximum = eval(input())
#     getOff = input().split(",")
#     getIn = input().split(",")
#     for i in range(amount):
#         getOff[i] = eval(getOff[i])
#         getIn[i] = eval(getIn[i])
#     return getOff, getIn, amount, maximum


# def run(getOff, getIn, amount, maximum, curStation = 0, curPpl = 0, code = []):
#     while curStation < amount:
#         global ppl
#         ppl = nextStation(getOff, getIn, curStation, curPpl)
#         code.append(isReasonable(ppl, maximum))
#         curStation += 1
#     return ppl, code

# def nextStation(Off, In, curStation, curPpl):
#     currentPpl = curPpl
#     currentPpl -= Off[curStation]
#     currentPpl += In[curStation]
#     return currentPpl

# def isReasonable(curPpl, Max):
#     if curPpl < 0:
#         return 1
#     elif curPpl > Max:
#         return 2
#     else:
#         return 0

# def outPut(codeLs, PPL):
#     if 1 not in codeLs and 2 not in codeLs:
#         print("{},{}".format(PPL, 0))
#     else:
#         print("{},{}".format(PPL, codeLs[0]))

# main()

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
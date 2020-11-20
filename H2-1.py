num = input()
lt = []
for i in range(3):
    if len(num) == 1:
        num = "00" + num
    if len(num) == 2:
        num = "0" + num
    # 由大到小
    ls = []
    for i in range(len(num)):
        ls.append(int(num[i]))
    ls.sort()
    ls.reverse()
    largeToSmall = ""
    for i in range(len(ls)):
        largeToSmall += str(ls[i])
    largeToSmall = int(largeToSmall)
    # 由小到大
    ls = []
    for i in range(len(num)):
        ls.append(int(num[i]))
    ls.sort()
    smallToLarge = ""
    for i in range(len(ls)):
        smallToLarge += str(ls[i])
    smallToLarge = int(smallToLarge)
    num = str(largeToSmall - smallToLarge)
    lt.append(num)
print(",".join(lt))

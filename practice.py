# def TYPE(ls):
#     for i in range(len(ls)):
#         try:
#             for j in range(len(ls[i])):

#                 print("{}: numerical".format(j))
#         except Exception:
#             print("{}: categorical".format(j))
#     return 0
def maxlen(ls):
    for i in range(len(ls[0])):
        maximum = 0
        for j in range(len(ls)):
            length = len(ls[j][i])
            if length > maximum:
                maximum = length
        print("{}: {}".format(i, maximum))


def maxnumlen(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j][-1] == ".":
                ls[i][j] = ls[i][j].replace(".", ".0")
    print(ls)
    for i in range(len(ls[0])):
        index = 0
        for j in range(len(ls)):
            ask = ls[j][i].find(".")
            if ask > index:
                maximum = index
            elif ask == -1:
                maximum = 0
        print("{}: {}".format(i, index))


route = input()
mode = input()
with open(route, "r", encoding="cp950") as f1:
    f1 = f1.read()
    f1 = f1.split("\n")
    for i in range(len(f1)):
        f1[i] = f1[i].split(",")
    for i in range(len(f1)):
        for j in range(len(f1[i])):
            f1[i][j] = f1[i][j].replace(" ", "")
    if f1[-1] == ['']:
        f1 = f1[:-1]
    # print(f1)

if mode == "MAXLEN":
    maxlen(f1)
elif mode == "MAXNUMLEN":
    maxnumlen(f1)
else:
    print(0)

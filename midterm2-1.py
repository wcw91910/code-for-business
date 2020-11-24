def plotmirror(ls, way, loc=0):
    if way == "v":
        for i in range(len(ls)):
            for j in range(0, len(ls[i]), 2):
                dis = abs(ls[i][j] - loc)
                if ls[i][j] < loc:
                    ls[i][j] = ls[i][j] + 2*dis
                else:
                    ls[i][j] = ls[i][j] - 2*dis
    else:
        for i in range(len(ls)):
            for j in range(1, len(ls[i]), 2):
                dis = abs(ls[i][j] - loc)
                if ls[i][j] < loc:
                    ls[i][j] = ls[i][j] + 2*dis
                else:
                    ls[i][j] = ls[i][j] - 2*dis
    return ls


# 取得資料並且整理
points = []
while True:
    data = input()
    if data == "LINESTOP":
        break
    else:
        points.append(data.split(","))

for i in range(len(points)):
    for j in range(len(points[i])):
        points[i][j] = eval(points[i][j])
data1 = input().split(",")
mode = data1[0]
location = eval(data1[1])

# 最後輸出
finalList = plotmirror(points, mode, location)
for i in range(len(finalList)):
    print("Line{}: {:.3f} {:.3f} {:.3f} {:.3f}".format(i, finalList[i][0], finalList[i][1], finalList[i][2], finalList[i][3]))

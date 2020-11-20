import math


def rotate(linelist, degree=90):
    Sin = math.sin(math.radians(degree))
    Cos = math.cos(math.radians(degree))
    for i in range(len(linelist)):
        linelist[i][0], linelist[i][1] = linelist[i][0] * Cos + linelist[i][1] * (-Sin), linelist[i][0] * Sin + linelist[i][1] * Cos
        # linelist[i][1] = linelist[i][0] * Sin + linelist[i][1] * Cos
        linelist[i][2], linelist[i][3] = linelist[i][2] * Cos + linelist[i][3] * (-Sin), linelist[i][2] * Sin + linelist[i][3] * Cos
        # linelist[i][3] = linelist[i][2] * Sin + linelist[i][3] * Cos
    return linelist


def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


info = []
while True:
    data = input().split(",")
    if data[0] == "LINESTOP":
        break
    else:
        for i in range(len(data)):
            data[i] = float(data[i])
        info.append(data)
deg = float(input())
rotate(info, deg)
printlines(info)

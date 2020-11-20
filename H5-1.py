def plotshift(linelist, xshift=0, yshift=0):
    for i in range(len(linelist)):
        linelist[i][0] += xshift
        linelist[i][1] += yshift
        linelist[i][2] += xshift
        linelist[i][3] += yshift
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
move = input().split(",")
moveX = float(move[0])
moveY = float(move[1])
plotshift(info, moveX, moveY)
printlines(info)

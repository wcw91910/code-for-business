def player_avg(seasons, records, player_number):
    AB = 0
    H = 0
    for year in seasons:
        for info in records:
            if info[2] == year and info[1] == int(player_number):
                AB += info[3]
                H += info[4]
    return H / AB


def team_avg(seasons, records, team_name):
    AB = 0
    H = 0
    for year in seasons:
        for info in records:
            if info[2] == year and info[0] == team_name:
                AB += info[3]
                H += info[4]
    return H / AB


def best_player(seasons, records):
    bestList = []
    for year in seasons:
        bestNumber = 0
        bestRate = 0
        AB = 10000
        playerNum = 10000
        for info in records:
            if info[2] == year:
                rate = info[4] / info[3]
                if rate > bestRate:
                    bestRate = rate
                    bestNumber = info[1]
                    AB = info[3]
                    playerNum = info[1]
                elif rate == bestRate:
                    if info[3] < AB:
                        bestRate = rate
                        bestNumber = info[1]
                        AB = info[3]
                        playerNum = info[1]
                    elif info[3] == AB:
                        if info[1] < playerNum:
                            bestRate = rate
                            bestNumber = info[1]
                            AB = info[3]
                            playerNum = info[1]
        bestList.append(bestNumber)
    return bestList


def best_team(seasons, records):
    bestList = []
    for year in seasons:
        qualified = []
        bestRate = 0
        bestTeam = 0
        count = 10000
        name = "Z"
        for info in records:
            if info[2] == year:
                if info[0] not in qualified:
                    qualified.append(info[0])
        for team in qualified:
            H = 0
            AB = 0
            for info in records:
                if info[0] == team and info[2] == year:
                    H += info[4]
                    AB += info[3]
            rate = H / AB
            if rate > bestRate:
                bestRate = rate
                bestTeam = team
                count = AB
                name = team
            elif rate == bestRate:
                if AB < count:
                    bestRate = rate
                    bestTeam = team
                    count = AB
                    name = team
                elif AB == count:
                    if ord(team) < ord(name):
                        bestRate = rate
                        bestTeam = team
                        count = AB
                        name = team
        bestList.append(bestTeam)
    return bestList


def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0


# 先輸入球員資料
playerInfo = []
while True:
    data = input()
    if data == "RECORDSTOP":
        break
    else:
        data = data.split(",")
        for i in range(1, len(data)):
            data[i] = int(data[i])
        playerInfo.append(data)

# 輸入測試資料
testData = []
while True:
    data = input()
    if data == "FUNCTIONSTOP":
        break
    else:
        assignedOne = "N/A"
        data = data.split(" ")
        if len(data) == 2:
            mode = int(data[0])
            yr = data[1].split(",")
            for i in range(len(yr)):
                yr[i] = int(yr[i])
        elif len(data) == 3:
            mode = int(data[0])
            yr = data[1].split(",")
            for i in range(len(yr)):
                yr[i] = int(yr[i])
            assignedOne = data[2]
        testData.append([mode, yr, assignedOne])

# 計算資料
for stuff in testData:
    if stuff[0] == 1:
        averge = player_avg(stuff[1], playerInfo, stuff[2])
        print(chop(averge))
    elif stuff[0] == 2:
        averge = team_avg(stuff[1], playerInfo, stuff[2])
        print(chop(averge))
    elif stuff[0] == 3:
        best = best_player(stuff[1], playerInfo)
        for i in range(len(best)):
            best[i] = str(best[i])
        print(",".join(best))
    elif stuff[0] == 4:
        best = best_team(stuff[1], playerInfo)
        print(",".join(best))

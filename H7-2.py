try:
    # 輸入基本資料
    items = input()
    genres = input()
    movieID = eval(input()) - 1
    qualified = []
    classBelonged = []

    # 對資料進行分割並找出類別
    with open(items, mode="r", encoding="ISO-8859-1") as item:
        item = item.readlines()
        info = item[movieID].strip()
        info = info.split("|")
        for i in range(5, len(info)):
            if info[i] == "1":
                index = i
                qualified.append(index - 5)

    with open(genres, mode="r", encoding="ISO-8859-1") as genre:
        genre = genre.readlines()
        for i in range(len(genre)):
            genre[i] = genre[i].strip()
            genre[i] = genre[i].split("|")
        genre.pop(-1)
    for qualifiedItems in qualified:
        for classInfo in genre:
            if qualifiedItems == eval(classInfo[1]):
                classBelonged.append(classInfo[0])
                break
    print("{}: ".format(info[1]), end="")
    print(", ".join(classBelonged))
except Exception:
    print("No movie found.")

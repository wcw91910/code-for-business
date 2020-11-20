def qualifiedCompanies(cla, cat, ls):
    """找出符合產業的公司"""
    for info in cat:
        if info[1] == cla:
            ls.append(info[0])
    return ls


def countWeight(company, keywordWeight, tt, keywordWeightInTypeDict):
    """計算加權"""
    counter = {}
    keywordWeight = keywordWeight.items()
    for biaoTi in tt:
        biaoTi = biaoTi.strip()
        if company in biaoTi:
            replace = biaoTi
            keywordWeight = sorted(keywordWeight, key=lambda x: (len(x[0]), -replace.find(x[0])), reverse=True)
            for info in keywordWeight:
                keyword = info[0]
                times = 0
                while keyword in replace:
                    index = replace.find(keyword)
                    times += 1
                    replace = replace[:index] + "|"*len(keyword) + replace[index + len(keyword):]
                if times > 0:
                    counter[keyword] = counter.get(keyword, 0) + times
    total = 0
    for kWord in counter:
        total += counter[kWord]*eval(keywordWeightInTypeDict.get(kWord))
    return total


# 基本資料輸入和建立
titles = input()
dics = input()
categories = input()
data = input()
data = data.split(",")
Class = data[0]
total = data[1]
quantity = data[2].split(":")
qualified = []
keywordTimes = {}
rank = []

# 開啟檔案
with open(titles, mode="r", encoding="utf-8") as title:
    title = title.readlines()
    # 整理資料
    for i in range(len(title)):
        title[i] = title[i].strip()

with open(dics, mode="r", encoding="utf-8") as dic:
    dic = dic.readlines()
    # 整理資料
    for i in range(len(dic)):
        dic[i] = dic[i].split(" ")
        for j in range(len(dic[i])):
            dic[i][j] = dic[i][j].strip()
    dic = dict(dic)

with open(categories, mode="r", encoding="utf-8") as category:
    category = category.readlines()
    # 整理資料
    for i in range(len(category)):
        category[i] = category[i].split(" ")
        for j in range(len(category[i])):
            category[i][j] = category[i][j].strip()

# 對分數進行排名
qualified = qualifiedCompanies(Class, category,  qualified)
for company in qualified:
    score = countWeight(company, dic, title, dic)
    rank.append([company, score])
rank.sort(key=lambda x: (x[1], ord(x[0][1])), reverse=True)

# 進行最後輸出
if len(qualified) == 0:
    print("NO_MATCH")
else:
    if len(qualified) < len(quantity):
        quantity = quantity[:len(qualified)]
    buy = [0]*len(quantity)
    total = eval(total)
    while total > 0:
        for i in range(len(quantity)):
            if eval(quantity[i]) <= total:
                buy[i] += eval(quantity[i])
                total -= eval(quantity[i])
            else:
                buy[i] += total
                total = 0
                break
    for com in range(len(buy)):
        if buy[com] == 0:
            continue
        else:
            print("{}購買{}張".format(rank[com][0], buy[com]))

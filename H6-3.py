# 先讀入基本資料
companies = input().split(",")
keywords = input().split(",")
keywords.sort(key=lambda x: len(x), reverse=True)
titles = []
while True:
    data = input()
    if data == "INPUT_END":
        break
    else:
        data = data.replace(" ", "")
        titles.append(data)

# 對關鍵字進行分割
for i in range(len(titles)):
    replace = titles[i]
    ls = []
    for j in range(len(keywords)):
        ls.append(keywords[j])
    while True:
        if len(ls) == 0:
            break
        else:
            ls.sort(key=lambda x: (len(x), -replace.find(x)), reverse=True)
            keyword = ls[0]
            if keyword in replace:
                keywordIndex = replace.find(keyword)
                titles[i] = titles[i][:keywordIndex] + "/" + keyword + "/" + titles[i][keywordIndex + len(keyword):]
                replace = replace.replace(keyword, "|"*(len(keyword) + 2), 1)
            else:
                ls.pop(0)


for i in range(len(titles)):
    titles[i] = titles[i].replace("//", "/")
    # 去掉前後/
    if titles[i][0] == "/":
        titles[i] = titles[i][1:]
    if titles[i][-1] == "/":
        titles[i] = titles[i][:-1]

# 調整最後輸出格式
for title in titles:
    qualifiedCompanies = []
    for company in companies:
        if company in title:
            qualifiedCompanies.append(company)
    qualifiedCompanies.sort(key=lambda x: (title.count(x), -companies.index(x)), reverse=True)
    if len(qualifiedCompanies) == 0:
        print("NO_MATCH")
    else:
        print(",".join(qualifiedCompanies), end=";")
        print(title)

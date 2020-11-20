def findBeforeWord(File, keyword):
    count = {}
    for line in File:
        split = line.split("\t")
        for replace in split:
            replace = replace.strip()
            i = 0
            while keyword in replace[i:]:
                index = replace.find(keyword, i)
                if index > 0:
                    beforeWord = replace[index - 1]
                    count[beforeWord] = count.get(beforeWord, 0) + 1
                i = index + 1
    return count


def findNextWord(File, keyword):
    count = {}
    for line in File:
        split = line.split("\t")
        for replace in split:
            replace = replace.strip()
            i = 0
            while keyword in replace[i:]:
                index = replace.find(keyword, i)
                if index < len(replace) - len(keyword):
                    nextWord = replace[index + len(keyword)]
                    count[nextWord] = count.get(nextWord, 0) + 1
                i = index + 1
    return count


def sort(dictionary):
    dic = dictionary
    sorted_items = sorted(dic.items(), key=lambda x: (x[1], ord(x[0])), reverse=True)
    return sorted_items


# 輸入基本資料
fileLocation = input()
keyword = input()

# 開啟檔案並且計算
with open(fileLocation, mode="r", encoding="utf-8") as data:
    data = data.readlines()
dicBefore = findBeforeWord(data, keyword)
dicNext = findNextWord(data, keyword)
beforeList = sort(dicBefore)
nextList = sort(dicNext)

# 最後輸出
print("熱門前一個字:")
if len(beforeList) <= 10:
    for word in beforeList:
        print("{}---{}".format(word[0], keyword))
else:
    for i in range(10):
        print("{}---{}".format(beforeList[i][0], keyword))

print("熱門下一個字:")
if len(nextList) <= 10:
    for word in nextList:
        print("{}---{}".format(keyword, word[0]))
else:
    for i in range(10):
        print("{}---{}".format(keyword, nextList[i][0]))

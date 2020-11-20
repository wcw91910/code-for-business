distance = int(input())
keyword1 = input()
keyword2 = input()
output = []
minusSpace = []
keyword1Position = []
keyword2Position = []


def findPosition(keyword, String, PositionList):
    global replace
    replace = String  # 創造一個可被更改的字串, 使原始string不被動到
    while keyword in replace:
        index = replace.find(keyword)
        PositionList.append(index)
        replace = replace.replace(keyword, "|"*len(keyword), 1)
    return PositionList


# 串接字串
string = ""
while True:
    data = input()
    if data == "INPUT_END":
        break
    else:
        ls = []
        for word in data:
            ls.append(word)
        while ls[0] == " ":
            ls.remove(ls[0])
        while ls[-1] == " ":
            ls.remove(ls[-1])
        data = ""
        for i in ls:
            data += i
        string = string + data + " "
# 刪去字串最後一個空格
for word in string:
    minusSpace.append(word)
minusSpace.pop(-1)
string = ""
for i in minusSpace:
    string += i

# 取得關鍵字的index
keyword1Position = findPosition(keyword1, string, keyword1Position)
keyword2Position = findPosition(keyword2, string, keyword2Position)

# 把符合的index全部跑一遍，確認兩個詞中間的文字數量是否符合條件
for keyword1Index in keyword1Position:
    for keyword2Index in keyword2Position:
        if keyword2Index - keyword1Index - len(keyword1) <= distance and keyword2Index - keyword1Index - len(keyword1) >= 0:
            a = keyword1Index - 7
            b = keyword2Index + len(keyword2) + 7
            if a < 0:
                a = 0
            if b > len(replace):
                b = len(replace)
            sentence = string[a:keyword1Index] + "**" + keyword1 + "**" + string[keyword1Index + len(keyword1):keyword2Index] + "**" + keyword2 + "**" + string[(keyword2Index + len(keyword2)):b]
            output.append(sentence)

# 把符合條件的印出來
if len(output) == 0:
    print("NO_MATCH")
else:
    for item in output:
        print(item)

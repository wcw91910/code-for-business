keyword = input()
output = []
minusSpace = []

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

for word in string:
    minusSpace.append(word)
minusSpace.pop(-1)
string = ""
for i in minusSpace:
    string += i

replace = string  # 創造一個可被更改的字串, 使原始string不被動到
while keyword in replace:
    index = replace.find(keyword)
    a = index - 7
    b = index + len(keyword) + 7
    if a < 0:
        a = 0
    if b > len(replace):
        b = len(replace)
    sentence = string[a:index] + "**" + keyword + "**" + string[(index + len(keyword)):b]
    output.append(sentence)
    replace = replace.replace(keyword, "|"*len(keyword), 1)

if len(output) == 0:
    print("NO_MATCH")
else:
    for item in output:
        print(item)

# 建立數字中文對照
dic = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九", "10": "十", "+": "加", "-": "減", "*": "乘以", "/": "除以", "=": "等於"}

# 進行分割
ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(ls)):
    ls[i] = str(ls[i])
data = input()
oprater = []
for i in range(len(data)):
    if data[i] not in ls:
        oprater.append(data[i])
        data = data.replace(data[i], ",", 1)
num = data.split(",")

# 進行最後輸出
for i in range(len(num) - 1):
    if len(num[i]) == 2:
        if num[i][0] == "1":
            print("十" + dic[num[i][1]], end="")
        else:
            print(dic[num[i][0]] + "十" + dic[num[i][1]], end="")
    else:
        print(dic[num[i]], end="")
    print(dic[oprater[i]], end="")
if len(num[-1]) == 2:
    print(dic[num[-1][0]] + "十" + dic[num[-1][1]], end="")
else:
    print(dic[num[-1]], end="")

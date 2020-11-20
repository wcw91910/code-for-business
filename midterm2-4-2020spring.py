dic = {
    "zero":0,
    "one":1,
    "two":2, 
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "ten":10,
    "eleven":11,
    "twelve":12,
    "thirteen":13,
    "fourteen":14,
    "fifteen":15,
    "sixteen":16,
    "seventeen":17,
    "eighteen":18,
    "nineteen":19,
    "twenty":20,
    "thirty":30,
    "forty":40,
    "fifty":50,
    "sixty":60,
    "seventy":70,
    "eighty":80,
    "ninety":90
}
data = input().split(" ")
for i in range(len(data)):
    if "-" in data[i]:
        data[i] = data[i].split("-")
if "plus" in data:
    data.remove("plus")
    # print(data)
    for i in range(len(data)):
        if len(data[i]) == 2:
            data[i] = dic[data[i][0]] + dic[data[i][1]]
        else:
            data[i] = dic[data[i]]
    print(data[0] + data[1])
else:
    data.remove("minus")
    # print(data)
    for i in range(len(data)):
        if len(data[i]) == 2:
            data[i] = dic[data[i][0]] + dic[data[i][1]]
        else:
            data[i] = dic[data[i]]
    print(data[0] - data[1])

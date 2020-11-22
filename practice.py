import operator
import time
with open(file="C:\\this\\Gossiping-QA-Dataset.txt", mode="r", encoding="utf-8") as f:
    lines = f.readlines()
keyword = input()
sta = time.perf_counter()
before = []
after = []
for i in range(len(lines)):
    locationlst = []
    if lines[i].find(keyword) == '-1':
        i += 1
        pass
    else:
        emplines = lines[i]
        for j in range(int(lines[i].count(keyword))):
            location = int(emplines.find(keyword))
            locationlst.append(location)
            for m in range(len(keyword)):
                emplines = emplines.replace(emplines[location], '鞥', 1)
            j += 1
        for k in range(len(locationlst)):
            if locationlst[k] != (len(lines[i]) - len(keyword)) and locationlst[k] != 0:
                before.append(lines[i][locationlst[k] - 1])
                after.append(lines[i][locationlst[k] + len(keyword)])
            elif locationlst[k] == 0:
                after.append(lines[i][locationlst[k] + len(keyword)])
            elif locationlst[k] == (len(lines[i]) - len(keyword)):
                before.append(lines[i][locationlst[k] - 1])
        i += 1
        pass
modify = before.count('\t')
if modify == 0:
    pass
else:
    for m in range(modify):
        before.remove('\t')

dic_before = dict()
dic_after = dict()
for i in range(len(before)):
    e = before[i]
    dic_before[e] = before.count(before[i])
for i in range(len(after)):
    f = after[i]
    dic_after[f] = after.count(after[i])

sorted_before = sorted(dic_before.items(), key=operator.itemgetter(0), reverse=True)
sorted_after = sorted(dic_after.items(), key=operator.itemgetter(0), reverse=True)
sorted_former = sorted(sorted_before, key=lambda s: s[1], reverse=True)
sorted_latter = sorted(sorted_after, key=lambda s: s[1], reverse=True)

print('熱門前一個字：')
if len(sorted_former) >= 10:
    for i in range(10):
        print(sorted_former[i][0]+'---'+str(keyword))
else:
    for i in range(len(sorted_former)):
        print(sorted_former[i][0]+'---'+str(keyword))
print('熱門下一個字：')
if len(sorted_latter) >= 10:
    for i in range(10):
        print(str(keyword)+'---'+sorted_latter[i][0])
else:
    for i in range(len(sorted_latter)):
        print(str(keyword)+'---'+sorted_latter[i][0])
print(time.perf_counter() - sta)
ls = []
work = []
employee = []
final = []
length = eval(input())
for i in range(length):
    ls.append(input().split(","))
for i in range(length):
    for j in range(length):
        ls[i][j] = eval(ls[i][j])
for i in range(length):
    work.append(i)
    employee.append(i)
# print(work, employee)
# for i in range(length):
#     print(ls[i])
while len(work) != 0:
    smallest = 2**15
    for i in employee:
        for j in work:
            if ls[i][j] < smallest:
                smallest = ls[i][j]
                indexI = i
                indexJ = j
                Sum = i + j
            elif ls[i][j] == smallest:
                if i + j < Sum:
                    smallest = ls[i][j]
                    indexI = i
                    indexJ = j
                    Sum = i + j
                elif i + j == Sum:
                    if i < indexI:
                        smallest = ls[i][j]
                        indexI = i
                        indexJ = j
                        Sum = i + j
    employee.remove(indexI)
    work.remove(indexJ)
    final.append([indexI + 1, indexJ + 1, ls[indexI][indexJ]])
# print(final)
final.sort()
# print(final)
total = 0

lt = []
for i in final:
    lt.append(str(i[1]))
    total += i[2]
print(",".join(lt), end=";")
print(total)

data1 = input().split(",")
x = eval(data1[0])
y = eval(data1[1])
availableDistance = eval(data1[2])
population = []
for i in range(y + 1):
    data = input().split(",")
    for i in range(len(data)):
        data[i] = eval(data[i])
    population.append(data)
finalAnswer = 0
for u in range(x + 1):
    for v in range(y + 1):
        total = []
        hospitalX = u
        hospitalY = v
        for i in range(x + 1):
            for j in range(y + 1):
                if abs(i - u) + abs(j - v) <= availableDistance:
                    total.append(population[i][j])
        Sum = 0
        for ppl in range(len(total)):
            Sum += total[ppl]
        if Sum > finalAnswer:
            finalAnswer = Sum
print(finalAnswer)

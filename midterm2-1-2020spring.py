def main():
    vec = getData()
    ls = getDistances(vec)
    print(getSmallest(ls))


def getData():
    vectors = []
    row, column = eval(input())
    for i in range(row):
        vector = input().split(",")
        vectors.append(vector)
    for i in range(len(vectors)):
        for j in range(len(vectors[i])):
            vectors[i][j] = eval(vectors[i][j])
    return vectors


def countDistance(vec1, vec2):
    distance = 0
    for i in range(len(vec1)):
        distance += (vec1[i] - vec2[i])**2
    return distance


def getDistances(data):
    distances = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            else:
                dis = countDistance(data[i], data[j])
                distances.append(dis)
    return distances


def getSmallest(disList):
    disList.sort()
    smallest = disList[0]
    return smallest


main()
# print(getDistances([[1, 1, 1, 1], [2, 2, 3, 4], [4, 4, 9, 9]]))
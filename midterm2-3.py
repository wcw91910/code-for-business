# def TYPE(ls):
#     for i in range(len(ls)):
#         try:
#             for j in range(len(ls[i])):

#                 print("{}: numerical".format(j))
#         except Exception:
#             print("{}: categorical".format(j))
#     return 0
def maxlen(ls):
    for i in range(len(ls[0])):
        maximum = 0
        for j in range(len(ls)):
            length = len(ls[j][i])
            if length > maximum:
                maximum = length
        print("{}: {}".format(i, maximum))
        
file1 = "C:\\Users\\User\\Downloads\\PBC109_1_midterm2\\PBC109_1_midterm2\\midterm2_q3_sample1.txt"
file2 = "C:\\Users\\User\\Downloads\\PBC109_1_midterm2\\PBC109_1_midterm2\\midterm2_q3_sample2.txt"
with open(file2, "r", encoding="cp950") as f1:
    f1 = f1.read()
    f1 = f1.split("\n")
    # print(f1[len(f1) - 1])
    # f1[len(f1)  - 1] = f1[len(f1) - 1][:-1]
    # print(f1[-1])
    for i in range(len(f1)):
        f1[i] = f1[i].split(",")
    for i in range(len(f1)):
        for j in range(len(f1[i])):
            f1[i][j] = f1[i][j].replace(" ", "")
    if f1[-1] == ['']:
        f1 = f1[:-1]
    print(f1)

maxlen(f1)
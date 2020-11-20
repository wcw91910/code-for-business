data1 = input().split(",")
merchantsAmount = eval(data1[0])
commodityAmount = eval(data1[1])
transactionTimes = eval(data1[2])
demandedItem = eval(data1[3])
transaction = []
for i in range(transactionTimes):
    data = input().split(",")
    for i in range(len(data)):
        data[i] = eval(data[i])
    transaction.append(data)  # 依序為商人編號，商品編號，評分
# print(transaction)
# print(merchantsAmount, commodityAmount, transactionTimes, demandedItem)
qualified = []
for i in range(transactionTimes):
    if transaction[i][1] == demandedItem:
        qualified.append([transaction[i][2], transaction[i][0]])
qualified.sort(reverse=True)
largest = qualified[0][0]
# print(qualified)
# print(largest)
answer = []
for i in range(len(qualified)):
    if qualified[i][0] == largest and (qualified[i][1]) not in answer:
        answer.append(qualified[i][1])
print("{}".format(largest), end=":")
for i in range(len(answer)):
    answer[i] = str(answer[i])
answer.sort()
print(",".join(answer))

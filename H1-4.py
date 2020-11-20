PM25 = int(input())
temp = int(input())
dewTemp = int(input())
limit = float(input())
if PM25 <= 35:
    willingOfPollution = 0.5+(100-PM25)*0.005
else:
    willingOfPollution = 0.5+(45-PM25)*0.02
humid = 100-5*(temp-dewTemp)
if humid <= 30:
    willingOfHumid = (110-humid)/120
else:
    willingOfHumid = (90-humid)/90
if willingOfPollution < 0:
    willingOfPollution = 0
if willingOfHumid < 0:
    willingOfHumid = 0
if willingOfPollution > 1:
    willingOfPollution = 1
if willingOfHumid > 1:
    willingOfHumid = 1
# 選擇相對較小的意願值
if willingOfPollution < willingOfHumid:
    willing = willingOfPollution
else:
    willing = willingOfHumid
print("{:.2f}".format(willing))
if willing >= limit:
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")

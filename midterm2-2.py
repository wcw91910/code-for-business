final = ""
# 進行處理
while True:
    data = input()
    if data == "INPUTSTOP":
        break
    else:
        data = data.strip()
        while "  " in data:
            data = data.replace("  ", " ")
        data = data.replace(",", ",")
        data = data.replace(" , ", ", ")
        data = data.replace(" ,", ", ")
        data = data.replace(":", ": ")
        data = data.replace(" : ", ":")
        data = data.replace(" :", ": ")
        data = data.replace(".", ". ")
        data = data.replace(" .", ". ")
        data = data.replace(" . ", ". ")
        while "  " in data:
            data = data.replace("  ", " ")
        data = data.strip()
        while '"' in data:
            if data.count('"') == 1:
                break
            else:
                data = data.replace('"', "「", 1)
                data = data.replace('"', "」", 1)
        print(data)

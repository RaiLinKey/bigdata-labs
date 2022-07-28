with open("office.txt", "r") as f:
    for line in f.readlines():
        sym_arr = line.strip().split(",-")
        sym_arr[0] = int(sym_arr[0])
        print(sym_arr)

import pyhdfs


def CCP():
    fs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")
    f = fs.open("/user/kali/lab2/outputCCP/part-00000")
    arr = []
    for line in f:
        strin = ", ".join(line.decode()[0:-1].split("\t"))
        pairs = strin.split(", ")
        pairs[2] = int(pairs[2])
        arr.append(pairs)

    arr.sort(key=lambda x: x[2], reverse=True)

    # for item in arr:
    #     print(item)

    check_word = input("Write item's name: ")
    count = 0
    for i in range(len(arr)):
        if check_word.lower() == arr[i][0].lower():
            count += 1
            print(f"{count}:\t{arr[i][1]}:  {arr[i][2]}")
        elif check_word.lower() == arr[i][1].lower():
            count += 1
            print(f"{count}:\t{arr[i][0]}:  {arr[i][2]}")
        if count == 10:
            break

import pyhdfs
import operator


def CCS():
    fs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")
    f = fs.open("/user/kali/lab2/outputCCS/part-00000")
    arr = []
    for line in f:
        strin = line.decode()[0:-1].split("\t")
        strin[1] = eval(strin[1])
        strin[1] = dict(sorted(strin[1].items(), key=operator.itemgetter(1), reverse=True))
        arr.append(strin)

    check_word = input("Write item's name: ")
    count = 0
    for item in arr:
        if check_word.lower() == item[0].lower():
            for dict_item in item[1]:
                count += 1
                print(f"{count}: {dict_item}:  {item[1][dict_item]}")
                if count == 10:
                    break

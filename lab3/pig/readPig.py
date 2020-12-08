import pyhdfs

fs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")


def req1():
    with fs.open("/pigresult/req1/part-r-00000") as f:
        for line in f.readlines():
            data = line.decode().strip().split("\t")
            print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[4]}\t{data[12]}")  # max id 12


def req2():
    with fs.open("/pigresult/req2/part-r-00000") as f:
        for line in f.readlines():
            data = line.decode().strip().split("\t")
            print(f"{data[0]}\t{data[1]}\t{data[4]}\t{data[5]}")


def req3():
    with fs.open("/pigresult/req3/part-r-00000") as f:
        for line in f.readlines():
            data = line.decode().strip().split("\t")
            print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[4]}\t{data[7]}")


def req4():
    with fs.open("/pigresult/req4/part-m-00000") as f:
        for line in f.readlines():
            print(line.decode().strip())


def req5():
    with fs.open("/pigresult/req5/part-m-00000") as f:
        for line in f.readlines():
            data = line.decode().strip().split("\t")
            print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[5]}")


while True:
    listener = input("What's result (req1, req2, req3, req4, req5): ")
    if listener == "req1":
        req1()
    elif listener == "req2":
        req2()
    elif listener == "req3":
        req3()
    elif listener == "req4":
        req4()
    elif listener == "req5":
        req5()
    elif listener == "exit":
        break
    else:
        print("Input ERROR!")

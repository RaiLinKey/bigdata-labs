import pyhdfs

dfs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")


def get_info(req_num):
    with dfs.open(f"/user/kali/lab3/mrReq{req_num}/part-00000") as fs:
        for line in fs.readlines():
            print(line.decode().strip())


while True:
    listener = input("What's result (req1, req2, req3, req4, req5): ")
    if listener == "req1":
        get_info(1)
    elif listener == "req2":
        get_info(2)
    elif listener == "req3":
        get_info(3)
    elif listener == "req4":
        get_info(4)
    elif listener == "req5":
        get_info(5)
    elif listener == "exit":
        break
    else:
        print("Input ERROR!")

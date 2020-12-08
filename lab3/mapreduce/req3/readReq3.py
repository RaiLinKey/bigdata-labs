import pyhdfs

dfs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")
with dfs.open("/user/kali/lab3/mrReq3/part-00000") as fs:
    for line in fs.readlines():
        print(line.decode().strip())

#!/usr/bin/python3
import pyhdfs

fs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")

# fs.delete("/user/kali/PBFS")
# fs.delete("/user/kali/lab4")
fs.copy_from_local("/home/kali/mysources/lab5/tweets.csv", "/user/kali/tweets/input/tweets.csv")

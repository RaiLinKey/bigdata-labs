import pyhdfs

fs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")

fs.copy_from_local("/home/kali/mysources/lab3/deploy/office", "/user/kali/input/office/office")
fs.copy_from_local("/home/kali/mysources/lab3/deploy/work_place", "/user/kali/input/work_place/work_place")
fs.copy_from_local("/home/kali/mysources/lab3/deploy/workers", "/user/kali/input/workers/workers")

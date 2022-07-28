#!/usr/bin/python3
import sys
import pyhdfs
from math import sqrt

username = "kali"
fs = pyhdfs.HdfsClient(hosts='127.0.0.1:50070', user_name=username)
with fs.open('/user/kali/lab4/HITS/hub/part-00000') as f:
    for line in f.readlines():
        sum_hub = line.decode().strip().split('\t')[1]

for line in sys.stdin:
    key, values = line.strip().split('\t')
    graph, auth, hub = values.split(';')
    print(f'{key}\t({graph});{auth};{float(hub)/sqrt(float(sum_hub))}')

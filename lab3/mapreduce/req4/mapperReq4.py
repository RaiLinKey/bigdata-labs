#!/usr/bin/python3
import sys

for _line in sys.stdin:
    data = _line.strip().split('\t')
    if int(data[5]) >= 150000:
        print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[4]}\t{data[5]}\t{data[6]}")

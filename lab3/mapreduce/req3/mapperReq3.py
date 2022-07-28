#!/usr/bin/python3
import sys

for _line in sys.stdin:
    data = _line.strip().split('\t')
    if len(data) == 3:
        new_data = [int(data[0]), ["wp", [data[1]]]]
        print(new_data)
    else:
        new_data = [int(data[6]), ["workers", [data[0], data[1], data[2], data[3], data[4]]]]
        print(new_data)

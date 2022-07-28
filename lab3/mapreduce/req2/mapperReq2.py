#!/usr/bin/python3
import sys

for _line in sys.stdin:
    data = _line.strip().split('\t')
    if data[2].isnumeric():
        new_data = [int(data[2]), ["wp", [int(data[0]), data[1]]]]
        print(new_data)
    else:
        new_data = [int(data[0]), ["office", [data[1], data[2]]]]
        print(new_data)

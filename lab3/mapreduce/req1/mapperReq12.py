#!/usr/bin/python3
import sys

for _line in sys.stdin:
    data = _line.strip().split('\t')
    if len(data) == 3:
        print(f'{int(data[0])}\t{["office", [data[2]]]}')
    else:
        print(f'{int(data[5])}\t{["workers_wp", [data[0], data[1], data[2], data[3], data[4]]]}')

#!/usr/bin/python3
import sys

sum = 0
for line in sys.stdin:
    sum += float(line.strip().split('\t')[1].split(';')[2])**2
print(f'{0}\t{sum}')

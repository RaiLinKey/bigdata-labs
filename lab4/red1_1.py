#!/usr/bin/python3
import sys
from math import sqrt

sum_auth = 0
for line in sys.stdin:
    key, values = line.strip().split('\t')
    sum_auth += float(values)

print(f'{0}\t{sum_auth}')

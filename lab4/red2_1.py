#!/usr/bin/python3
import sys
from math import sqrt

sum_hub = 0
for line in sys.stdin:
    key, values = line.strip().split('\t')
    sum_hub += float(values)

print(f'{0}\t{sum_hub}')

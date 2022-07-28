#!/usr/bin/python3
import sys

for line in sys.stdin:
    key, values = line.strip().split('\t')
    graph, auth, hub = values.split(';')
    for i in eval(graph):
        print(f'{i}\t{key};{auth};{hub}')
    print(f'{key}\t{auth}')

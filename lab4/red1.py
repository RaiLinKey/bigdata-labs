#!/usr/bin/python3
import sys

last_key, graph, auth_sum = None, list(), 0
for line in sys.stdin:
    key, values = line.strip().split('\t')
    if last_key and last_key != key:
        print(f'{last_key}\t({",".join(graph)});{auth_sum};{v}')
        graph = list()
        if ';' in values:
            gr, auth, hub = values.strip().split(';')
            graph.append(gr)
            auth_sum = float(hub)
        else:
            v = values
            auth_sum = 0
    elif ';' in values:
        gr, auth, hub = values.strip().split(';')
        graph.append(gr)
        auth_sum += float(hub)
    else:
        v = values
    last_key = key

if last_key:
    print(f'{last_key}\t({",".join(graph)});{auth_sum};{v}')


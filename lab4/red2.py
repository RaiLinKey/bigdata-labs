#!/usr/bin/python3
import sys

last_key, graph, hub_sum = None, list(), 0
for line in sys.stdin:
    key, values = line.strip().split('\t')
    if last_key and last_key != key:
        print(f'{last_key}\t({",".join(graph)});{a};{hub_sum}')
        graph = list()
        if ';' in values:
            gr, auth, _ = values.strip().split(';')
            graph.append(gr)
            hub_sum = float(auth)
        else:
            a = values
            hub_sum = 0
    elif ';' in values:
        gr, auth, _ = values.strip().split(';')
        graph.append(gr)
        hub_sum += float(auth)
    else:
        a = values
    last_key = key

if last_key:
    print(f'{last_key}\t({",".join(graph)});{a};{hub_sum}')


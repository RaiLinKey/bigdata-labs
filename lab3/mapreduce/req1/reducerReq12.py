#!/usr/bin/python3
import sys

tag1 = "office"
tag2 = "workers_wp"
h = {}


def emit(t):
    for key in list(t.keys()):
        office = []
        workers = []
        for i in range(len(t[key])):
            if list(t[key][i].keys())[0] == tag1:
                office = t[key][i][tag1][0]
            elif list(t[key][i].keys())[0] == tag2:
                workers = t[key][i][tag2]
        for worker in workers:
            print(f"{worker[0]}\t{worker[1]}\t{worker[2]}\t{worker[3]}\t{worker[4]}\t{office[0]}")


for _line in sys.stdin:
    data = _line.strip().split("\t")
    key = int(data[0])
    tagged_tuple = eval(data[1])
    if not h:
        h.update({key: [{tagged_tuple[0]: [tagged_tuple[1]]}]})
    else:
        if key in list(h.keys()):
            for i in range(len(h[key])):
                if tagged_tuple[0] == list(h[key][i].keys())[0]:
                    h[key][i][tagged_tuple[0]].append(tagged_tuple[1])
                elif len(h[key]) == 1:
                    h[key].append({tagged_tuple[0]: [tagged_tuple[1]]})
        else:
            emit(h)
            h = {}
            h.update({key: [{tagged_tuple[0]: [tagged_tuple[1]]}]})

emit(h)

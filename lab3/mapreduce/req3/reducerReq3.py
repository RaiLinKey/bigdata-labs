#!/usr/bin/python3
import sys

tag1 = "wp"
tag2 = "workers"
h2 = {}
for _line in sys.stdin:
    data = eval(_line.strip())
    data_keys = list(data.keys())
    for key in data_keys:
        h = {}
        for i in range(len(data[key])):
            if not h or data[key][i][0] not in list(h.keys()):
                h.update({data[key][i][0]: [data[key][i][1]]})
            else:
                h[data[key][i][0]].append(data[key][i][1])  # {sample_name: [values]}
        if not h2 or key not in list(h2.keys()):
            h2.update({key: [h]})
        elif h2[key][0] and list(h2[key][0].keys())[0] == list(h.keys())[0]:
            h2[key][0][list(h.keys())[0]].append(h[list(h.keys())[0]][0])
        elif len(h2[key]) > 1:
            if list(h2[key][1].keys())[0] == list(h.keys())[0]:
                h2[key][1][list(h.keys())[0]].append(h[list(h.keys())[0]][0])
        else:
            h2[key].append(h)

for key in list(h2.keys()):
    wp = h2[key][1][tag1][0]
    # sys.stderr.write(str(wp) + "\n")
    for worker in h2[key][0][tag2]:
        # sys.stderr.write(str(worker) + "\n")
        print(f"{worker[0]}\t{worker[1]}\t{worker[2]}\t{worker[3]}\t{worker[4]}\t{wp[0]}")





#!/usr/bin/python3
import sys

h = {}
for _line in sys.stdin:
    data = eval(_line.strip())
    key = data[0]
    tagged_tuple = data[1]
    if not h or key not in list(h.keys()):
        h.update({key: [tagged_tuple]})
    else:
        h[key].append(tagged_tuple)

print(h)

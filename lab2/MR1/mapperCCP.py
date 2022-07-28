#!/usr/bin/python3
import sys


def first_mapping():
    pairs = []
    for _line in sys.stdin:
        basket = _line.strip().split(", ")
        for c_item in range(len(basket) - 1):
            for c2_item in range(c_item + 1, len(basket)):
                pair = [basket[c_item], basket[c2_item]]
                pair.sort()
                pairs.append(pair)  # print
    return pairs


out_pairs = first_mapping()
for k in out_pairs:
    line = ", ".join(k)
    print(line + "\t1")

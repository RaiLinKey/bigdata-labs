#!/usr/bin/python3.8
import sys
import operator

for _line in sys.stdin:
    basket = _line.strip().split(", ")
    for c_item in range(len(basket)):
        stripe = {basket[c_item]: {}}
        for c_item2 in range(len(basket)):
            if c_item == c_item2:
                continue
            else:
                stripe[basket[c_item]].update({basket[c_item2]: 1})
        stripe[basket[c_item]] = dict(sorted(stripe[basket[c_item]].items(), key=operator.itemgetter(0)))
        # print(stripe)
        # data_string = str(stripe[basket[c_item]]).replace("'", "").replace("{", "").replace("}", "")
        print(f"{basket[c_item]}\t{stripe[basket[c_item]]}")

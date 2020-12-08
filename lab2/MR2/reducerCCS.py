#!/usr/bin/python3.8
import sys
from collections import Counter


def fun1():
    (lastKey, sum_value) = (None, Counter())

    for line in sys.stdin:
        data = line.strip().split("\t")
        think = data[0]
        stripe = eval(data[1])
        stripe[list(stripe.keys())[0]] = int(stripe[list(stripe.keys())[0]])
        stripe = Counter(stripe)
        (key, value) = (think, stripe)
        if lastKey and lastKey != key:
            print(lastKey + '\t' + str(dict(sum_value)))
            (lastKey, sum_value) = (key, value)
        else:
            (lastKey, sum_value) = (key, sum_value + value)

    if lastKey:
        print(lastKey + '\t' + str(dict(sum_value)))


fun1()

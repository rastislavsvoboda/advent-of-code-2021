from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 1

start = datetime.now()
lines = open('1.in').readlines()


def solve1(lines):
    res = 0

    prev = None
    XS = [int(line) for line in lines]
    for x in XS:
        if prev and x > prev:
            res += 1
        prev = x

    return res


def solve2(lines):
    res = 0

    XS = [int(line) for line in lines]
    for i in range(len(XS)):
        if i >= 3 and (XS[i] + XS[i-1] + XS[i-2]) > (XS[i-1] + XS[i-2] + XS[i-3]):
            res += 1

    return res


print(solve1(lines))  # 1393
print(solve2(lines))  # 1359

stop = datetime.now()
print("duration:", stop - start)

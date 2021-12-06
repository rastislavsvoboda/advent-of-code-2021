from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 6

start = datetime.now()
lines = open('6.in').readlines()
# lines = open('6.in0').readlines()


def solve1(lines):
    line = lines[0].strip()
    nums = re.findall(r"[+-]?\d+", line)
    NUMS = [int(n) for n in nums]

    # print(NUMS)

    d = 0
    while d < 80:
        new = []
        app = []
        for n in NUMS:
            n -= 1
            if n == -1:
                new.append(6)
                app.append(8)
            else:
                new.append(n)
        NUMS = new + app
        d += 1
        # print("after ", d)
        # print(NUMS)

    res = len(NUMS)
    return res


def solve2(lines):
    line = lines[0].strip()
    nums = re.findall(r"[+-]?\d+", line)
    NUMS = [int(n) for n in nums]

    # print(NUMS)

    D = defaultdict(int)
    for n in NUMS:
        D[n] += 1

    # print(D)

    d = 0
    while d < 256:
        D2 = defaultdict(int)
        for k in D.keys():
            if k > 0:
                D2[k-1] = D[k]

        reset = D[0]
        D2[6] += reset
        D2[8] += reset

        d += 1
        D = D2
        # print(d)
        # print(D)

    res = sum(D.values())
    return res


print(solve1(lines))  # 343441
print(solve2(lines))  # 1569108373832

stop = datetime.now()
print("duration:", stop - start)

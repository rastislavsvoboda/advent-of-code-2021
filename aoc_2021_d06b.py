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


def solve(lines, days):
    line = lines[0].strip()
    nums = re.findall(r"\d+", line)
    NUMS = [int(n) for n in nums]

    D = defaultdict(int)
    for n in NUMS:
        D[n] += 1

    for d in range(days):
        D2 = defaultdict(int)
        for k,v in D.items():
            if k > 0:
                D2[k-1] += v
            else:
                # Each day, a 0 becomes a 6 and adds a new 8
                D2[6] += v
                D2[8] += v

        d += 1
        D = D2
        # print(d)
        # print(D)

    res = sum(D.values())
    return res


# print(solve(lines, 18))  # 343441
print(solve(lines, 80))  # 343441
print(solve(lines, 256))  # 1569108373832

stop = datetime.now()
print("duration:", stop - start)

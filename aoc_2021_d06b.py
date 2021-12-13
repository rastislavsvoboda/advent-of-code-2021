from datetime import datetime
from collections import defaultdict

# pypy3.exe .\save.py 6

start = datetime.now()
lines = open('6.in').readlines()
# lines = open('6.ex1').readlines()


def solve(lines, days):
    NUMS = [int(n) for n in lines[0].split(',')]

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

        D = D2
        # print(d+1, D)

    res = sum(D.values())
    return res


print(solve(lines, 80))  # 343441
print(solve(lines, 256))  # 1569108373832

stop = datetime.now()
print("duration:", stop - start)

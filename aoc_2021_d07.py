from datetime import datetime
import re

# pypy3.exe .\save.py 7

start = datetime.now()
lines = open('7.in').readlines()
# lines = open('7.in0').readlines()


def cost1(h1, h2):
    dist = abs(h1-h2)
    return dist


def cost2(h1, h2):
    dist = abs(h1-h2)
    return sum([i for i in range(0, dist+1)])


def solve(nums, minN, maxN, cost_fun):
    F = {}
    for h in range(minN, maxN+1):
        s = sum(cost_fun(x, h) for x in nums)
        F[h] = s

    return min(F.values())


line = lines[0].strip()
nums = re.findall(r"\d+", line)
N = [int(n) for n in nums]
minN = min(N)
maxN = max(N)

print(solve(N, minN, maxN, cost1))  # 349769
print(solve(N, minN, maxN, cost2))  # 99540554

stop = datetime.now()
print("duration:", stop - start)

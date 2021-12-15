from datetime import datetime
from collections import defaultdict, deque, Counter
import heapq

# pypy3.exe .\save.py 15

start = datetime.now()
lines = open('15.in').readlines()
# lines = open('15.ex1').readlines()


M = []
for line in lines:
    line = line.strip()
    M.append([int(c) for c in line])
# print(M)

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
R = len(M)
C = len(M[0])


def solve1():
    res = None
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    seen = set()
    while len(heap):
        risk, r, c = heapq.heappop(heap)
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if r == R-1 and c == C-1:
            res = risk
            break

        for i in range(4):
            rr = r + DR[i]
            cc = c + DC[i]
            if rr < 0 or rr >= R or cc < 0 or cc >= C:
                continue
            # Q.append((risk+M[rr][cc],(rr,cc)))
            heapq.heappush(heap, (risk+M[rr][cc], rr, cc))

    return res


def risk2(r, c):
    # each time the tile repeats to the right or downward,
    # all of its risk levels are 1 higher than the tile immediately up or left of it.
    # However, risk levels above 9 wrap back around to 1.
    newRisk = M[r % R][c % C] + r // R + c // C
    if newRisk > 9:
        newRisk -= 9
    return newRisk


def print_risk2():
    RT = R * 5
    CT = C * 5
    for r in range(RT):
        for c in range(CT):
            print(risk2(r, c), end='')
        print()


def solve2():
    res = None
    # the entire cave is actually five times larger in both dimensions
    RT = R * 5
    CT = C * 5
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    seen = set()
    res = None
    while len(heap):
        risk, r, c = heapq.heappop(heap)
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if r == RT-1 and c == CT-1:
            res = risk
            break

        for i in range(4):
            rr = r + DR[i]
            cc = c + DC[i]
            if rr < 0 or rr >= RT or cc < 0 or cc >= CT:
                continue
            heapq.heappush(heap, (risk+risk2(rr, cc), rr, cc))
    return res


# print_risk2()
print(solve1())  #
print(solve2())


stop = datetime.now()
print("duration:", stop - start)

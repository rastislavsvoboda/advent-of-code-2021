from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 9

start = datetime.now()
lines = open('9.in').readlines()
# lines = open('9.in0').readlines()
# lines = open('9.in1').readlines()



def is_lower_adj(r,c,F):
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr >= 0 and rr < len(F) and cc >= 0 and cc < len(F[rr]):
            if F[r][c] >= F[rr][cc]:
                return False

    return True



def solve1(lines):
    res = 0

    F=[]
    for line in lines:
        line = line.strip()
        row = [int(w) for w in line]
        F.append(row)

    # print(F)
    L=[]
    for r in range(len(F)):
        lst = []
        for c in range(len(F[r])):
            # print(r,c)
            low = is_lower_adj(r,c,F)
            if low: 
                res += F[r][c] + 1
            lst.append(low)
        L.append(lst)

    # for r in L:
    #     print(r)

    # print(L)
    return res


def count_sum(r,c,F):

    Q = deque()
    Q.append((r,c,F[r][c]))

    X = set()
    X.add((r,c))

    seen = set()
    s = 1
    while len(Q) > 0:
        (rr,cc,prev) = Q.popleft()
        # print(rr,cc,prev)

        if (rr,cc,prev) in seen:
            continue

        if rr<0 or rr>=len(F):
            continue

        if cc<0 or cc>=len(F[rr]):
            continue

        # print(rr,cc)
        e = F[rr][cc]

        if e == 9:
            continue

        if e > prev:
            X.add((rr,cc))
            # s+= 1

        seen.add((rr,cc,prev))

        Q.append((rr-1,cc,e))
        Q.append((rr+1,cc,e))
        Q.append((rr,cc-1,e))
        Q.append((rr,cc+1,e))

    # print(X)
    return len(X)


def solve2(lines):
    res = 0

    F=[]
    for line in lines:
        line = line.strip()
        row = [int(w) for w in line]
        F.append(row)

    # print(F)
    S=[]
    L=[]

    LOWS=[]

    for r in range(len(F)):
        lst = []
        for c in range(len(F[r])):
            # print(r,c)
            low = is_lower_adj(r,c,F)
            if low: 
                res += F[r][c] + 1
                LOWS.append((r,c))
            lst.append(low)
        L.append(lst)


    S=[]
    for (r,c) in LOWS:
        s = count_sum(r,c,F)
        S.append(s)

    S.sort()
    assert(len(S) >=3)
    # print(S)    


    # print(S[-1], S[-2], S[-3])
    res = S[-1] * S[-2] * S[-3]

    return res


print(solve1(lines))  # 560
print(solve2(lines))  # 959136

stop = datetime.now()
print("duration:", stop - start)
from datetime import datetime
from collections import defaultdict, deque, Counter
import copy
import re

# pypy3.exe .\save.py 20

start = datetime.now()
lines = open('20.in').readlines()
# lines = open('20.ex1').readlines()


def get_pix(r,c,data):
    if (r,c) in data:
        return data[(r,c)]
    return "."

def read_dec(r,c,data):
    r1=[get_pix(r-1, c, data) for c in range(c-1,c+2)]
    r2=[get_pix(r+0, c, data) for c in range(c-1,c+2)]
    r3=[get_pix(r+1, c, data) for c in range(c-1,c+2)]

    val = r1+r2+r3
    bin=[0 if v=='.' else 1 for v in val]
    bin_str = "".join(str(b) for b in bin)
    val_dec = int(bin_str,2)
    return val_dec

def print_data(data):
    rows = list(map(lambda p: p[0], data.keys()))
    cols = list(map(lambda p: p[1], data.keys()))

    r1=min(rows)
    r2=max(rows)
    c1=min(cols)
    c2=max(cols)

    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            val = data[(r,c)] if (r,c) in data else '.'
            print(val, end='')
        print()


def solve1(lines):
    res = 0

    alg = lines[0].strip()
    # print(alg)
    # print()


    G={}
    D=[]
    for line in lines[2:]:
        line = line.strip()
        D.append([c for c in line])
    # print(D)

    for r in range(len(D)):
        for c in range(len(D[r])):
            if D[r][c] == '#':
                G[(r,c)] = '#'
    # print(G)

    # val = read_dec(2,2,G)
    # print(alg[val])

    # rows = list(map(lambda p: p[0], G.keys()))
    # cols = list(map(lambda p: p[1], G.keys()))

    # r1=min(rows)
    # r2=max(rows)
    # c1=min(cols)
    # c2=max(cols)

    print_data(G)

    for s in range(2):
        G2={}
        rows = list(map(lambda p: p[0], G.keys()))
        cols = list(map(lambda p: p[1], G.keys()))

        r1=min(rows)
        r2=max(rows)
        c1=min(cols)
        c2=max(cols)
        print(r1,r2,c1,c2)

        for r in range(r1-1,r2+2):
            for c in range(c1-1,c2+2):
                val = read_dec(r,c,G)
                trans = alg[val]
                G2[(r,c)] = trans
        G = G2
        print()
        print_data(G)

    res = sum([1 for v in G.values() if v == '#'])        
    return res




print(solve1(lines))  # not correct: 5294
# print(solve1_t(text))  #
# print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)
from datetime import datetime
from collections import defaultdict
from typing import NewType

# pypy3.exe .\save.py 14

start = datetime.now()
lines = open('14.in').readlines()
# lines = open('14.ex1').readlines()


def solve1(lines):
    template = [x for x in lines[0].strip()]
    data = {}
    for line in lines[2:]:
        line = line.strip()
        words = line.split(' -> ')
        assert words[0] not in data
        data[words[0]] = words[1]
    # print(data)

    for s in range(10):
        template2 = [template[0]]
        for (a, b) in zip(template, template[1:]):
            template2.append(data[a+b])
            template2.append(b)
        template = template2
        # print("after ", s+1, template)

    C = defaultdict(int)
    for e in template:
        C[e] += 1
    return max(C.values()) - min(C.values())


def solve2(lines):
    template = lines[0].strip()
    data = {}
    for line in lines[2:]:
        line = line.strip()
        words = line.split(' -> ')
        assert words[0] not in data
        data[words[0]] = words[1]
    # print(data)

    C1 = defaultdict(int)
    for i in range(len(template)-1):
        C1[template[i:i+2]] += 1
    # print(C1)

    # ! counting idea from Jonathan Paulson
    for s in range(40):
        C2 = defaultdict(int)
        for c in C1:
            # when XY -> Z
            # there are 2 new pairs XZ, ZY
            newE1 = c[0] + data[c]
            C2[newE1] += C1[c]
            newE2 = data[c] + c[1]
            C2[newE2] += C1[c]
        C1 = C2
        # print("after ", s+1, C1)

    C = defaultdict(int)
    for c in C1:
        # for XY pairs, only count first X element
        C[c[0]] += C1[c]
    # add 1 for last character
    C[template[-1]] += 1
    return max(C.values()) - min(C.values())


print(solve1(lines))  # 2915
print(solve2(lines))  # 3353146900153

stop = datetime.now()
print("duration:", stop - start)

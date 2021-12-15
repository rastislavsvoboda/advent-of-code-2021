from datetime import datetime
from collections import Counter

# pypy3.exe .\save.py 14

start = datetime.now()
lines = open('14.in').readlines()
# lines = open('14.ex1').readlines()


def step1(template, data):
    new_template = [template[0]]
    for (a, b) in zip(template, template[1:]):
        new_template.append(data[a+b])
        new_template.append(b)
    return new_template


def solve1(lines):
    template = [x for x in lines[0].strip()]
    data = {}
    for line in lines[2:]:
        x, y = line.strip().split(' -> ')
        data[x] = y
    # print(data)

    for s in range(10):
        template = step1(template, data)
        # print("after ", s+1, template)

    C = Counter(template)
    return max(C.values()) - min(C.values())


def step2(counter, data):
    new_counter = Counter()
    for c in counter:
        # when XY -> Z
        # for each XY, there are 2 new pairs: XZ, ZY
        new_counter[c[0] + data[c]] += counter[c]
        new_counter[data[c] + c[1]] += counter[c]
    return new_counter


def solve2(lines):
    template = lines[0].strip()
    data = {}
    for line in lines[2:]:
        x, y = line.strip().split(' -> ')
        data[x] = y
    # print(data)

    # do frequency analysis on pairs
    C = Counter([template[i:i+2] for i in range(len(template)-1)])
    # C = Counter(map(lambda a,b: a+b, template, template[1:]))
    # print(C)

    for s in range(40):
        C = step2(C, data)
        # print("after ", s+1, C)

    # count single elements
    C_single = Counter()
    for c in C:
        C_single[c[0]] += C[c]
        C_single[c[1]] += C[c]
    # each middle char is counted twice, so add 1 for first and last char, and divide each by 2
    C_single[template[0]] += 1
    C_single[template[-1]] += 1
    counts = [c//2 for c in C_single.values()]
    return max(counts) - min(counts)


print(solve1(lines))  # 2915
print(solve2(lines))  # 3353146900153

stop = datetime.now()
print("duration:", stop - start)

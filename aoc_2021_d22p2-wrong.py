from datetime import datetime
from collections import defaultdict, deque, Counter
import copy
import re

# pypy3.exe .\save.py 22

start = datetime.now()
lines = open('22.in').readlines()
lines = open('22.ex1').readlines()
# lines = open('22.ex2').readlines()
# lines = open('22.ex3').readlines()

# text = open('22.in').read()


# def get_data(text):
#     data = []
#     for grp in text.split('\n\n'):
#         entries = []
#         for row in grp.split():
#             entries.append(row)
#         data.append(parse_entry(entries))
#     return data

# def parse_entry(entries):
#     # answers = []
#     # for entry in entries:
#     #     answers.append(set(entry))
#     # return answers
#     return entries

def solve1(lines):
    res = 0

    G = set()
    for line in lines:
        line = line.strip()
        words = line.split()
        nums = [int(v) for v in re.findall(r"[+-]?\d+", line)]
        x1, x2, y1, y2, z1, z2 = nums

        to_on = True if line.startswith('on') else False
        # print(line)
        # print(to_on,x1,x2,y1,y2,z1,z2)

        if x1 < -50:
            x1 = 50
        if x2 > 50:
            x2 = -50

        if y1 < -50:
            y1 = 50
        if y2 > 50:
            y2 = -50

        if z1 < -50:
            z1 = 50
        if z2 > 50:
            z2 = -50

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    if to_on:
                        G.add((x, y, z))
                    else:
                        if (x, y, z) in G:
                            G.remove((x, y, z))

        print(len(G))

        res = len(G)

    return res


def solve2(lines):
    res = 0

    ON_X = []
    ON_Y = []
    ON_Z = []

    for line in lines:
        line = line.strip()
        words = line.split()
        nums = [int(v) for v in re.findall(r"[+-]?\d+", line)]
        x1, x2, y1, y2, z1, z2 = nums

        to_on = True if line.startswith('on') else False

        x = (x1, x2)
        y = (y1, y2)
        z = (z1, z2)

        ON_X = merge(ON_X, x, to_on)
        ON_Y = merge(ON_Y, y, to_on)
        ON_Z = merge(ON_Z, z, to_on)

        res=0
        lengths_x = [(b-a)+1 for a, b in ON_X]
        lengths_y = [(b-a)+1 for a, b in ON_Y]
        lengths_z = [(b-a)+1 for a, b in ON_Z]

        for x in lengths_x:
            for y in lengths_y:
                for z in lengths_z:
                    res += x*y*z
        # print(res)

    return res


def merge(lst, line, state):
    res = []

    if state:
        if len(lst) == 0:
            res.append(line)

        else:
            x1, x2 = line

            starts = [x for (x, y) in lst] + [x1]
            ends = [y for (x, y) in lst] + [x2]

            cstarts = Counter(starts)
            cends = Counter(ends)

            xs = set(starts + ends)
            xs_sorted = list(xs)
            xs_sorted.sort()

            cnt = 0
            merged_s = None
            merged_e = None

            for x in xs_sorted:
                cnt += (cstarts[x] - cends[x])
                # if cnt == 0:
                #     res.append((x, x))
                if cnt > 0:
                    if merged_s is None:
                        merged_s = x
                else:
                    # if cnt == 0 and merged_s is not None:
                    #     res.append((x, x))
                    # else:
                    if merged_s is None:
                        merged_s = x

                    assert merged_s is not None
                    res.append((merged_s, x))
                    merged_s = None
    else:
        if len(lst) == 0:
            pass
        else:
            e1, e2 = line
            for x1, x2 in lst:
                if x2 < e1 or x1 > e2:
                    res.append((x1, x2))
                elif e1 <= x1 and x2 <= e2:
                    continue
                elif x1 < e1 and e1 <= x2:
                    res.append((x1, e1-1))
                elif x1 <= e2:
                    res.append((e2+1, x2))
                else:
                    assert False

    return res


def get_xs(D):
    X1s = [x1 for flag, x1, x2, y1, y2, z1, z2 in D]
    X2s = [x2 for flag, x1, x2, y1, y2, z1, z2 in D]
    X_all = X1s + X2s
    X_uniq = set(X_all)
    X_all = list(X_all)
    X_all.sort()
    print(X_all)

    return X_uniq


def is_inside(cub1, cub2):
    ax1, ax2, ay1, ay2, az1, az2 = cub1
    bx1, bx2, by1, by2, bz1, bz2 = cub2
    return (ax1 <= bx1 and bx2 <= ax2) and (ay1 <= by1 and by2 <= ay2) and (az1 <= bz1 and bz2 <= az2)


def is_overlap(cub1, cub2):
    ax1, ax2, ay1, ay2, az1, az2 = cub1
    bx1, bx2, by1, by2, bz1, bz2 = cub2
    return (ax1 <= bx1 <= ax2) and (bx1 <= ax2 <= bx2) and (ay1 <= by1 <= ay2) and (by1 <= ay2 <= by2) and (az1 <= bz1 <= az2) and (bz1 <= az2 <= bz2)


# print(merge([],(3,4),True))
# print(merge([(1,2)],(3,4),True))
# print(merge([(1,2)],(2,4),True))
# print(merge([(1,2),(3,4)],(3,4),True))
# print(merge([(1,2),(3,4)],(4,5),True))
# print(merge([(1,5),(6,10)],(4,5),True))
# print(merge([(1,5),(6,10)],(5,6),True))
# print(merge([(1,5),(6,10)],(4,7),True))
# print(merge([(1,5),(6,10)],(0,11),True))
# print(merge([(12,13)],(10,10),True))

# print(merge([],(3,4),False))
# print(merge([(1,2)],(3,4),False))
# print(merge([(1,2),(3,4)],(3,4),False))
# print(merge([(1,5),(6,10)],(4,5),False))
# print(merge([(1,5),(6,10)],(5,6),False))
# print(merge([(1,5),(6,10)],(4,7),False))
# print(merge([(1,5),(6,10)],(0,11),False))
# print(merge([(1,5),(6,7),(8,10)],(5,8),False))
# print(merge([(1,5),(6,7),(8,10)],(4,9),False))

# print(merge([(1,5),(6,7),(8,10)],(0,1),False))
# print(merge([(1,5),(6,7),(8,10)],(9,11),False))


# print(merge([(1,5),(6,10)],(4,5),True))
# print(merge([(1,5),(6,10)],(5,6),True))
# print(merge([(1,5),(6,10)],(4,7),True))
# print(merge([(1,5),(6,10)],(0,11),True))


print(solve1(lines))  # 545118
print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations

# pypy3.exe .\save.py 19

start = datetime.now()
text = open('19.in').read()
# text = open('19.ex1').read()
# text = open('19.ex2').read()


def get_data(text):
    data = []
    for grp in text.split('\n\n'):
        entries = []
        for row in grp.split():
            entries.append(row)
        data.append(parse_entry(entries))
    return data


def parse_entry(entries):
    coords = []
    scanner_id = int(entries[2])
    for entry in entries[4:]:
        x,y,z = [int(n) for n in entry.split(',')]
        coords.append((x,y,z))
    return (scanner_id, coords)


def transform(p, indx):
    x, y, z = p

    trans = [
        (x, y, z),
        (y, -x, z),
        (-x, -y, z),
        (-y, x, z),

        (-x, y, -z),
        (y,  x, -z),
        (x, -y, -z),
        (-y, -x, -z),

        (z,  y, -x),
        (y, -z, -x),
        (-z, -y, -x),
        (-y, z, -x),

        (-z, y, x),
        (y, z, x),
        (z, -y, x),
        (-y, -z, x),

        (x, z, -y),
        (z, -x, -y),
        (-x, -z, -y),
        (-z, x, -y),

        (-x, z, y),
        (z, x, y),
        (x, -z, y),
        (-z, -x, y)
    ]

    return trans[indx]


def p_to_str(p):
    x, y, z = p
    return f'{x},{y},{z}'


def find_common(points0, points1):
    D0 = defaultdict(set)
    S0D = []
    cmbs0 = list(combinations(points0, 2))
    for cmb in cmbs0:
        p1, p2 = cmb
        d = diff(p1, p2)
        S0D.append(d)
        k = p_to_str(d)
        D0[k].add(p1)
        D0[k].add(p2)
    # print(S0D)

    D1 = defaultdict(set)
    S1D = []
    cmbs1 = list(combinations(points1, 2))
    for cmb in cmbs1:
        p1, p2 = cmb
        d = diff(p1, p2)
        S1D.append(d)
        k = p_to_str(d)
        D1[k].add(p1)
        D1[k].add(p2)
    # print(S1D)

    s0s = set()
    for x in S0D:
        s0s.add(p_to_str(x))

    s1s = set()
    for x in S1D:
        s1s.add(p_to_str(x))

    over = s0s.intersection(s1s)
    # print(over)
    # print(len(over))

    C0 = set()
    C1 = set()
    for x in over:
        C0.update(D0[x])
        C1.update(D1[x])

    if len(over) < 66:
        return False, [], []

    C0L = list(C0)

    C1L = []

    init_diff = p_to_str(diff(C0L[0], C0L[1]))
    # print("init dif ", init_diff)
    cand1 = D1[init_diff]
    # print("candidates for first pos:", cand1)
    for c in cand1:
        # print("trying first", c)
        C1L = []
        C1L.append(c)
        isOk = True
        for i in range(1, len(C0L)):
            diff_to_find = p_to_str(diff(C0L[i-1], C0L[i]))
            next_cand = D1[diff_to_find]
            # print("next_cand", next_cand)

            # print("C1L", C1L[i-1] in next_cand)

            assert len(next_cand) == 2

            item = C1L[i-1]

            rest = [x for x in next_cand if x != item]
            # print("rest", rest)
            if len(rest) != 1:
                isOk = False
                break
            C1L.append(rest[0])
        if not isOk:
            continue
        if len(C1L) == len(C1):
            break

    # print(C1L)

    return True, C0L, C1L


def manhattan_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x1-x2)+abs(y1-y2) + abs(z1-z2)


def diff(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return [abs(x1-x2), abs(y1-y2), abs(z1-z2)]


def offset(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return [x1-x2, y1-y2, z1-z2]


def solve(text):
    data = get_data(text)

    N = len(data)
    # print(N)

    FINAL = {}
    FINAL[0] = (0, 0, 0)
    GOOD = {}
    for i in range(N):
        GOOD[i] = [x for x in range(24)]
    # assume that scanner 0 is not transformed and it uses (x,y,z)
    # so only this transform is possible for scanner 0
    GOOD[0] = [0]

    seen = set()
    Q = deque()
    Q.append(0)
    while len(Q) > 0:
        s0 = Q.popleft()
        seen.add(s0)

        sid0, points0 = data[s0]
        others = [s for s in range(N) if s != s0 and s not in seen]
        for s1 in others:
            sid1, points1 = data[s1]
            for i in GOOD[s0]:
                for j in GOOD[s1]:
                    trans_points0 = list(map(lambda p: transform(p, i), points0))
                    trans_points1 = list(map(lambda p: transform(p, j), points1))
                    found, common_points0, common_points1 = find_common(trans_points0, trans_points1)
                    if found:
                        # compute all offsets between common points
                        offsets = set()
                        for a, b in zip(common_points0, common_points1):
                            offsets.add(tuple(offset(a, b)))
                        if len(offsets) == 1:
                            # if it is the same offset for all points
                            # this is correct transformation
                            single_offset = offsets.pop()
                            print(f"good transformation for {s0} ({i}), {s1} ({j}), offset {single_offset}")
                            if s1 not in seen:
                                Q.append(s1)
                                GOOD[s1] = [j]
                                x1, y1, z1 = FINAL[s0]
                                x2, y2, z2 = single_offset
                                FINAL[s1] = (x2+x1, y2+y1, z2+z1)

    # print(FINAL)

    # all bacons relative to scanner 0 
    all_bacons = set()
    for s, points in data:
        for p in points:
            # transformed bacon point using scanner's transform
            xb, yb, zb = transform(p, GOOD[s][0])
            # scanner offset
            xs, ys, zs = FINAL[s]
            # point transformed to scanner 0
            x0, y0, z0 = xb + xs, yb + ys, zb + zs
            all_bacons.add((x0, y0, z0))

    res1 = len(all_bacons)

    distances = []
    for s0 in range(N):
        for s1 in range(N):
            if s0 < s1:
                distances.append(manhattan_distance(FINAL[s0], FINAL[s1]))

    res2 = max(distances)

    return res1, res2


print(solve(text))  # 479, 13113

stop = datetime.now()
print("duration:", stop - start)

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


def transform(point, index):
    x, y, z = point

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

    return trans[index]


def p_to_str(p):
    x, y, z = p
    return f'{x},{y},{z}'


def compute_differences(points):
    differences = defaultdict(set)
    point_combinations = list(combinations(points, 2))
    for (p1, p2) in point_combinations:
        diff_str = p_to_str(diff(p1, p2))
        differences[diff_str].add(p1)
        differences[diff_str].add(p2)
    return differences


def find_common(points0, points1):
    differences0 = compute_differences(points0)
    differences1 = compute_differences(points1)
    overlapping = set(differences0.keys()) & set(differences1.keys())

    # 66 is combinations for 12 points
    if len(overlapping) < 66:
        # not enough overlapping bacons
        return False, [], []

    # create set of points that are in both scanners
    common_points_set0 = set()
    common_points_set1 = set()
    for diff_str in overlapping:
        common_points_set0.update(differences0[diff_str])
        common_points_set1.update(differences1[diff_str])

    # create common_points_list1 such both lists contains matching points in correct order
    # compute differences pairwise between points in common_points_list0
    # and find appropriate points to fill into common_points_list1
    common_points_list0 = list(common_points_set0)
    common_points_list1 = []
    init_diff = p_to_str(diff(common_points_list0[0], common_points_list0[1]))
    candidates = differences1[init_diff]
    for point_candidate in candidates:
        common_points_list1 = []
        common_points_list1.append(point_candidate)
        isOk = True
        for i in range(1, len(common_points_list0)):
            diff_to_find = p_to_str(diff(common_points_list0[i-1], common_points_list0[i]))
            next_candidates = differences1[diff_to_find]
            # assuming there is no same difference between more than 2 points
            assert len(next_candidates) == 2
            prev_point = common_points_list1[i-1]
            # the other points
            other_points = next_candidates - set([prev_point])
            if len(other_points) != 1:
                isOk = False
                break
            # if single left, this is the correct point
            common_points_list1.append(other_points.pop())
        if not isOk:
            continue
        if len(common_points_list1) == len(common_points_set1):
            break

    assert len(common_points_list1) == len(common_points_set1)

    return True, common_points_list0, common_points_list1


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

    # final positions of the scanners
    scanner_positions = {}
    scanner_positions[0] = (0, 0, 0)

    # good tranformation available for each scanner
    scanner_transformations = {}
    for i in range(N):
        scanner_transformations[i] = [x for x in range(24)]
    # scanner 0 is at (0,0,0) so any transf. is the same
    # so assume it is transf. 0 with (x,y,z)
    scanner_transformations[0] = [0]

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
            for i in scanner_transformations[s0]:
                for j in scanner_transformations[s1]:
                    trans_points0 = [transform(p, i) for p in points0]
                    trans_points1 = [transform(p, j) for p in points1]
                    found, common_points0, common_points1 = find_common(trans_points0, trans_points1)
                    if found:
                        # compute all offsets between common points and put it in set
                        offsets = set([tuple(offset(a, b)) for a, b in zip(common_points0, common_points1)])
                        if len(offsets) == 1:
                            # if it is the same offset for all points
                            # this is correct transformation
                            single_offset = offsets.pop()
                            print(f"good transformation for {s0} ({i}), {s1} ({j}), offset {single_offset}")
                            if s1 not in seen:
                                Q.append(s1)
                                # assuming when found that only one transf. is correct,
                                # but stored as list for enable iterating
                                scanner_transformations[s1] = [j]
                                # using prev. scanner position to witch we are comparing to
                                x1, y1, z1 = scanner_positions[s0]
                                # and current offset
                                x2, y2, z2 = single_offset
                                # compute final position for this scanner
                                scanner_positions[s1] = (x2+x1, y2+y1, z2+z1)

    # all bacons relative to scanner 0 
    all_bacons = set()
    for s, points in data:
        for p in points:
            # transformed bacon point using scanner's transform
            xb, yb, zb = transform(p, scanner_transformations[s][0])
            # scanner offset
            xs, ys, zs = scanner_positions[s]
            # point transformed to scanner 0
            x0, y0, z0 = xb + xs, yb + ys, zb + zs
            all_bacons.add((x0, y0, z0))

    res1 = len(all_bacons)

    distances = []
    for s0 in range(N):
        for s1 in range(N):
            if s0 < s1:
                distances.append(manhattan_distance(scanner_positions[s0], scanner_positions[s1]))

    res2 = max(distances)

    return res1, res2


print(solve(text))  # 479, 13113

stop = datetime.now()
print("duration:", stop - start)

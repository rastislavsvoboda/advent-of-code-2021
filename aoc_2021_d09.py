from datetime import datetime
from collections import deque

# pypy3.exe .\save.py 9

start = datetime.now()
lines = open('9.in').readlines()
# lines = open('9.in0').readlines()
# lines = open('9.in1').readlines()


def is_lower_adj(r, c, F):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr >= 0 and rr < len(F) and cc >= 0 and cc < len(F[rr]):
            if F[r][c] >= F[rr][cc]:
                return False

    return True


def solve1(data):
    low_points = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if is_lower_adj(r, c, data):
                low_points.append((r, c))

    risk_levels = []
    for (r, c) in low_points:
        # The risk level of a low point is 1 plus its height
        risk_levels.append(1 + data[r][c])

    return sum(risk_levels)


def count_area(r, c, F):
    coords = set()
    coords.add((r, c))
    seen = set()
    Q = deque()
    Q.append((r, c, F[r][c]))
    while len(Q) > 0:
        (rr, cc, prev) = Q.popleft()

        if (rr, cc, prev) in seen:
            continue

        seen.add((rr, cc, prev))

        if rr >= 0 and rr < len(F) and cc >= 0 and cc < len(F[rr]):
            curr = F[rr][cc]

            # Locations of height 9 do not count
            if curr == 9:
                continue

            if curr > prev:
                coords.add((rr, cc))

            Q.append((rr-1, cc, curr))
            Q.append((rr+1, cc, curr))
            Q.append((rr, cc-1, curr))
            Q.append((rr, cc+1, curr))

    # print(coords)
    return len(coords)


def solve2(data):
    low_points = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if is_lower_adj(r, c, data):
                low_points.append((r, c))

    basin_sizes = []
    for (r, c) in low_points:
        basin_sizes.append(count_area(r, c, data))

    basin_sizes.sort(reverse=True)
    assert(len(basin_sizes) >= 3)
    # print(basin_sizes)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


data = [[int(x) for x in line.strip()] for line in lines]
print(solve1(data))  # 560
print(solve2(data))  # 959136

stop = datetime.now()
print("duration:", stop - start)

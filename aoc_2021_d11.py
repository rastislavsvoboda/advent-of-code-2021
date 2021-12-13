from datetime import datetime
from collections import deque

# pypy3.exe .\save.py 11

start = datetime.now()
lines = open('11.in').readlines()
# lines = open('11.ex1').readlines()
# lines = open('11.ex2').readlines()


def get_data(lines):
    return [[int(x) for x in line.strip()] for line in lines]


def print_data(data):
    for r in data:
        print(r)


def step(data):
    R = len(data)
    C = len(data[0])
    flashed = set()
    Q = deque()

    # initial increase, Q is prepared with coords to flash
    for r in range(R):
        for c in range(C):
            data[r][c] += 1
            if data[r][c] > 9:
                Q.append((r, c))

    while Q:
        r, c = Q.popleft()
        if (r, c) in flashed:
            continue
        flashed.add((r, c))

        # increase all neighbors, add them if they also going to flash
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            rr, cc = r + dr, c + dc
            if (0 <= rr < R) and (0 <= cc < C):
                data[rr][cc] += 1
                if data[rr][cc] > 9:
                    Q.append((rr, cc))

    # reset level of flashed to 0
    for (r, c) in flashed:
        data[r][c] = 0

    return len(flashed)


def solve1(lines):
    M = get_data(lines)
    # print_data(M)

    total_flashes = 0
    for i in range(100):
        # print("after ", i+1)
        total_flashes += step(M)
        # print_data(M)

    return total_flashes


def solve2(lines):
    M = get_data(lines)
    R = len(M)
    C = len(M[0])
    # print_data(M)
    # print(R, C)

    i = 0
    while True:
        i += 1
        # print("after ", i)
        num_flashes = step(M)
        # print_data(M)
        if (num_flashes == (R*C)):
            break

    return i


print(solve1(lines))  # 1697
print(solve2(lines))  # 344

stop = datetime.now()
print("duration:", stop - start)

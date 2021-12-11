from datetime import datetime
from collections import deque

# pypy3.exe .\save.py 11

start = datetime.now()
lines = open('11.in').readlines()
# lines = open('11.in0').readlines()
# lines = open('11.in1').readlines()


def get_data(lines):
    data = []
    for line in lines:
        m = []
        for c in line.strip():
            m.append(int(c))

        data.append(m)
    return data


def print_data(data):
    for r in data:
        print(r)


def flash(data):
    flashed = set()
    Q = deque()

    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] > 9:
                Q.append((r, c))

    while Q:
        r, c = Q.popleft()
        if (r, c) in flashed:
            continue

        if data[r][c] > 9:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if r+dr < 0 or r+dr >= len(data):
                        continue
                    if c+dc < 0 or c+dc >= len(data[0]):
                        continue
                    data[r+dr][c+dc] += 1
                    if data[r+dr][c+dc] > 9:
                        Q.append((r+dr, c+dc))
            flashed.add((r, c))

    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] > 9:
                data[r][c] = 0

    return len(flashed)


def solve1(lines):
    M = get_data(lines)
    # print_data(M)
    R = len(M)
    C = len(M[0])

    total_flashes = 0
    for i in range(100):
        for r in range(R):
            for c in range(C):
                M[r][c] += 1
        # print("after ", i+1)
        total_flashes += flash(M)
        # print_data(M)

    return total_flashes


def solve2(lines):
    M = get_data(lines)
    # print_data(M)
    R = len(M)
    C = len(M[0])

    i = 0
    while True:
        for r in range(R):
            for c in range(C):
                M[r][c] += 1
        i += 1
        # print("after ", i)
        num_flashes = flash(M)
        # print_data(M)
        if (num_flashes == (R*C)):
            break

    return i


print(solve1(lines))  # 1697
print(solve2(lines))  # 344

stop = datetime.now()
print("duration:", stop - start)

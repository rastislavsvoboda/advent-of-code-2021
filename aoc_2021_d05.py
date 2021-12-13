from datetime import datetime
from collections import defaultdict
import re

# pypy3.exe .\save.py 5

start = datetime.now()
lines = open('5.in').readlines()
# lines = open('5.ex1').readlines()


def print_diagram(diagram):
    mx = 0
    my = 0
    for k in diagram.keys():
        (y, x) = k
        if x > mx:
            mx = x
        if y > my:
            my = y

    for y in range(my+1):
        for x in range(mx+1):
            if diagram[(y, x)] == 0:
                print(".", end="")
            else:
                print(diagram[(y, x)], end="")
        print()


def solve(lines, part):
    D = defaultdict(int)

    for line in lines:
        nums = re.findall(r"\d+", line.strip())
        x1, y1 = int(nums[0]), int(nums[1])
        x2, y2 = int(nums[2]), int(nums[3])
        dx = 1 if x2 >= x1 else -1
        dy = 1 if y2 >= y1 else -1

        if x1 == x2:
            # vertical
            for y in range(y1, y2+dy, dy):
                D[(y, x1)] += 1
        elif y1 == y2:
            # horizontal
            for x in range(x1, x2+dx, dx):
                D[(y1, x)] += 1
        elif abs(x2-x1) == abs(y2-y1) and part == 2:
            # diagonal for part 2
            y = y1
            for x in range(x1, x2+dx, dx):
                D[y, x] += 1
                y += dy

    # print_diagram(D)

    res = sum(1 for v in D.values() if v >= 2)
    return res


print(solve(lines, 1))  # 5774
print(solve(lines, 2))  # 18423

stop = datetime.now()
print("duration:", stop - start)

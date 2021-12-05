from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 5

start = datetime.now()
lines = open('5.in').readlines()
# lines = open('5.in0').readlines()


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
    res = 0
    diagram = defaultdict(int)

    for line in lines:
        line = line.strip()
        nums = re.findall(r"\d+", line)
        x1, y1 = int(nums[0]), int(nums[1])
        x2, y2 = int(nums[2]), int(nums[3])

        if x1 == x2:
            # vertical
            dy = y2 >= y1 and 1 or -1
            for y in range(y1, y2+dy, dy):
                diagram[(y, x1)] += 1
        elif y1 == y2:
            # horizontal
            dx = x2 >= x1 and 1 or -1
            for x in range(x1, x2+dx, dx):
                diagram[(y1, x)] += 1
        elif abs(x2-x1) == abs(y2-y1) and part == 2:
            # diagonal for part 2
            dx = x2 >= x1 and 1 or -1
            dy = y2 >= y1 and 1 or -1

            y = y1
            for x in range(x1, x2+dx, dx):
                diagram[y, x] += 1
                y += dy

    # print_diagram(diagram)

    res = sum(1 for v in diagram.values() if v >= 2)
    return res


print(solve(lines, 1))  # 5774
print(solve(lines, 2))  # 18423

stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
import re

# pypy3.exe .\save.py 17

start = datetime.now()
lines = open('17.in').readlines()
# lines = open('17.ex1').readlines()


def step(x, y, x_vel, y_vel):
    x += x_vel
    y += y_vel

    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1

    y_vel -= 1

    return x, y, x_vel, y_vel


def try_solution(x_vel, y_vel, x1, x2, y1, y2):
    x, y = (0, 0)
    max_y = y
    s = 0
    while s < 500:
        x, y, x_vel, y_vel = step(x, y, x_vel, y_vel)
        s += 1

        if y > max_y:
            max_y = y


        if x1 <= x <= x2 and y1 <= y <= y2:
            return True, max_y

    return False, max_y


def solve(lines):
    res = 0

    nums = re.findall(r"[+-]?\d+", lines[0].strip())
    x1, x2, y1, y2 = int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])

    # print(x1,x2,y1,y2)

    x, y = (0, 0)
    OK = set()

    for xv in range(-500, 501):
        for yv in range(-500, 501):
            r = try_solution(xv, yv, x1, x2, y1, y2)
            if r[0]:
                print(r, xv, yv)
                res = max(res, r[1])
                OK.add((xv, yv))

    return res, len(OK)


print(solve(lines))  # p1 19503, p2 5200


stop = datetime.now()
print("duration:", stop - start)

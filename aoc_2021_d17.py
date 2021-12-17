from datetime import datetime
import re

# pypy3.exe .\save.py 17

start = datetime.now()
lines = open('17.in').readlines()
# lines = open('17.ex1').readlines()


def step(x, y, vx, vy):
    x += vx
    y += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    vy -= 1

    return x, y, vx, vy


def try_solution(vx, vy, x1, x2, y1, y2):
    x, y = (0, 0)
    max_y = y
    for _ in range(500):
        x, y, vx, vy = step(x, y, vx, vy)
        max_y = max(max_y, y)
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True, max_y
    return False, max_y


def solve(lines):
    numbers = re.findall(r"[+-]?\d+", lines[0].strip())
    x1, x2, y1, y2 = [int(n) for n in numbers]
    # print("target area:", x1,x2,y1,y2)

    highest_y = 0
    ok_velocities = set()

    for vx in range(-500, 501):
        for vy in range(-500, 501):
            ok, max_y = try_solution(vx, vy, x1, x2, y1, y2)
            if ok:
                print(vx, vy)
                highest_y = max(highest_y, max_y)
                ok_velocities.add((vx, vy))

    return highest_y, len(ok_velocities)


print(solve(lines))  # p1 19503, p2 5200


stop = datetime.now()
print("duration:", stop - start)

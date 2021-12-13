from datetime import datetime
from collections import defaultdict

# pypy3.exe .\save.py 13

start = datetime.now()
lines = open('13.in').readlines()
# lines = open('13.ex1').readlines()


def parse(lines):
    dots = defaultdict(bool)
    instructions = []
    nums = True
    for line in lines:
        line = line.strip()
        if line == '':
            nums = False
            continue
        if nums:
            words = line.split(',')
            x, y = int(words[0]), int(words[1])
            dots[(y, x)] = True
        else:
            words = line.split('=')
            n = int(words[1])
            if 'x' in words[0]:
                instructions.append(('x', n))
            else:
                instructions.append(('y', n))
    return dots, instructions


def fold_x(x, data):
    folded = {}
    for (r, c) in data:
        if c < x:
            folded[(r, c)] = True
        elif c > x:
            folded[(r, (2*x - c))] = True
    return folded


def fold_y(y, data):
    folded = {}
    for (r, c) in data:
        if r < y:
            folded[(r, c)] = True
        elif r > y:
            folded[((2*y - r), c)] = True
    return folded


def print_data(data, R, C, nice=False):
    for r in range(R):
        for c in range(C):
            if (r, c) in data:
                print('█' if nice else '#', end='')
            else:
                print(' ' if nice else '.', end='')
        print()


def solve1(lines):
    dots, instructions = parse(lines)
    R = max(dots.keys(), key=lambda p: p[0])[0]
    C = max(dots.keys(), key=lambda p: p[1])[1]
    # print_data(dots, R, C)

    # part 1 - process only first instruction
    (axis, n) = instructions[0]
    if axis == 'x':
        dots = fold_x(n, dots)
        C = C // 2
    else:
        dots = fold_y(n, dots)
        R = R // 2

    # print_data(dots, R, C)
    return len(dots)


def solve2(lines):
    dots, instructions = parse(lines)
    R = max(dots.keys(), key=lambda p: p[0])[0]
    C = max(dots.keys(), key=lambda p: p[1])[1]
    # print_data(dots, R, C)

    for (axis, n) in instructions:
        if axis == 'x':
            dots = fold_x(n, dots)
            C = C // 2
        else:
            dots = fold_y(n, dots)
            R = R // 2

    print_data(dots, R, C, nice=True)
    return None


print(solve1(lines))  # 763
print(solve2(lines))  # RHALRCRA


stop = datetime.now()
print("duration:", stop - start)

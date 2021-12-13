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
            if words[0][-1] == 'x':
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
            folded[(r, (x - (c-x)))] = True
    return folded


def fold_y(y, data):
    folded = {}
    for (r, c) in data:
        if r < y:
            folded[(r, c)] = True
        elif r > y:
            folded[((y - (r-y)), c)] = True
    return folded


def print_data(data, nice=False):
    R = max(data.keys(), key=lambda p: p[0])[0]
    C = max(data.keys(), key=lambda p: p[1])[1]
    for r in range(R+1):
        for c in range(C+1):
            if (r, c) in data:
                print('█' if nice else '#', end='')
            else:
                print(' ' if nice else '.', end='')
        print()


def solve1(lines):
    dots, instructions = parse(lines)
    # print_data(dots)

    # part 1 - process only first instruction
    (axis, n) = instructions[0]
    if axis == 'x':
        dots = fold_x(n, dots)
    else:
        dots = fold_y(n, dots)

    # print_data(dots)
    return len(dots)


def solve2(lines):
    dots, instructions = parse(lines)
    # print_data(dots)

    for (axis, n) in instructions:
        if axis == 'x':
            dots = fold_x(n, dots)
        else:
            dots = fold_y(n, dots)

    print_data(dots, nice=True)
    return None


print(solve1(lines))  # 763
print(solve2(lines))  # RHALRCRA


stop = datetime.now()
print("duration:", stop - start)

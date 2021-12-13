from datetime import datetime
from collections import defaultdict

# pypy3.exe .\save.py 13

start = datetime.now()
lines = open('13.in').readlines()
# lines = open('13.ex1').readlines()


def parse(lines):
    numbers = defaultdict(bool)
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
            numbers[(y, x)] = True
        else:
            words = line.split('=')
            n = int(words[1])
            if 'x' in words[0]:
                instructions.append(('x', n))
            else:
                instructions.append(('y', n))
    return numbers, instructions


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


def print_data(N, maxR, maxC, nice=False):
    for r in range(maxR):
        for c in range(maxC):
            if (r, c) in N:
                if nice:
                    print('█', end='')
                else:
                    print('#', end='')
            else:
                if nice:
                    print(' ', end='')
                else:
                    print('.', end='')
        print()


def solve1(lines):
    N, I = parse(lines)
    maxR = max(N.keys(), key=lambda x: x[0])[0]
    maxC = max(N.keys(), key=lambda x: x[1])[1]
    # print_data(N, maxR, maxC)

    # part 1 - process only first instruction
    (axis, n) = I[0]
    if axis == 'x':
        N = fold_x(n, N)
        maxC = maxC // 2
    else:
        N = fold_y(n, N)
        maxR = maxR // 2

    # print_data(N, maxR, maxC)
    return len(N)


def solve2(lines):
    N, I = parse(lines)
    maxR = max(N.keys(), key=lambda p: p[0])[0]
    maxC = max(N.keys(), key=lambda p: p[1])[1]
    # print_data(N, maxR, maxC)

    for (axis, n) in I:
        if axis == 'x':
            N = fold_x(n, N)
            maxC = maxC // 2
        else:
            N = fold_y(n, N)
            maxR = maxR // 2

    print_data(N, maxR, maxC, True)
    return None


print(solve1(lines))  # 763
print(solve2(lines))  # RHALRCRA


stop = datetime.now()
print("duration:", stop - start)

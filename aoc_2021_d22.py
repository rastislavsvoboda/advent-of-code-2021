from datetime import datetime
import re

# pypy3.exe .\save.py 22

start = datetime.now()
lines = open('22.in').readlines()
# lines = open('22.ex1').readlines()
# lines = open('22.ex2').readlines()
# lines = open('22.ex3').readlines()


def solve1(lines):
    G = set()
    for line in lines:
        numbers = [int(v) for v in re.findall(r"[+-]?\d+", line.strip())]
        x1, x2, y1, y2, z1, z2 = numbers
        turn_on = line.startswith('on')

        # keep data inside -50..50 range on each axes
        x1 = max(x1, -50)
        y1 = max(y1, -50)
        z1 = max(z1, -50)

        x2 = min(x2, 50)
        y2 = min(y2, 50)
        z2 = min(z2, 50)

        # keep track of ON values, ranges are not too big
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    if turn_on:
                        G.add((x, y, z))
                    elif (x, y, z) in G:
                        G.remove((x, y, z))

    return len(G)


def solve2(lines):
    D = []
    Xs = set()
    Ys = set()
    Zs = set()
    for line in lines:
        numbers = [int(v) for v in re.findall(r"[+-]?\d+", line.strip())]
        x1, x2, y1, y2, z1, z2 = numbers
        turn_on = line.startswith('on')
        D.append((x1, x2, y1, y2, z1, z2, turn_on))
        Xs.add(x1)
        Xs.add(x2+1)
        Ys.add(y1)
        Ys.add(y2+1)
        Zs.add(z1)
        Zs.add(z2+1)
    print("parsed, len=", len(D))

    # split axes to all possible values of X, Y, Z
    # when it can be different, if x1..x2, change can start at x1 till x2, so next change can be at x2+1
    # each segment will be ON or OFF,
    # instead of every single point, that is too much to keep track of
    X_segments, X_sizes = make_segments_and_sizes(Xs)
    Y_segments, Y_sizes = make_segments_and_sizes(Ys)
    Z_segments, Z_sizes = make_segments_and_sizes(Zs)
    print("segments done")

    G = set()
    for (x1, x2, y1, y2, z1, z2, turn_on) in D:
        # turn on/off all segments between x1..x2, y1..y2, z1..z2
        for ix in range(X_segments[x1], X_segments[x2+1]):
            for iy in range(Y_segments[y1], Y_segments[y2+1]):
                for iz in range(Z_segments[z1], Z_segments[z2+1]):
                    if turn_on:
                        G.add((ix, iy, iz))
                    elif (ix, iy, iz) in G:
                        G.remove((ix, iy, iz))
    print("assigning done")

    # sum the volumes of ON segments
    count_on = 0
    for (ix, iy, iz) in G:
        count_on += X_sizes[ix] * Y_sizes[iy] * Z_sizes[iz]

    return count_on


def make_segments_and_sizes(values):
    # prepare dictionary of segments and sizes
    # for example, if values after sorting are [1, 4, 7, 8, 10, 13]
    # segments:    sizes:
    # 1:  0        4-1=3
    # 4:  1        7-4=3
    # 7:  2        8-7=1
    # 8:  3        10-8=2
    # 10: 4        13-10=3
    # 13: 5        -
    
    # needs values of 1D coordinate in increasing order
    sorted_list = sorted(values)

    # segment maps value to index
    segments = {}
    for i, v in enumerate(sorted_list):
        segments[v] = i

    # size is pairwise difference
    sizes = [v2-v1 for v1, v2 in zip(sorted_list, sorted_list[1:])]

    return segments, sizes


print(solve1(lines))  # 545118
print(solve2(lines))  # 1227298136842375

stop = datetime.now()
print("duration:", stop - start)

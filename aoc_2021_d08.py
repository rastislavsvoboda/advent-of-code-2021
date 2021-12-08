from datetime import datetime

# pypy3.exe .\save.py 8

start = datetime.now()
lines = open('8.in').readlines()
# lines = open('8.in0').readlines()
# lines = open('8.in1').readlines()
# lines = open('8.in2').readlines()


def count_part1(left, right):
    # count how many right values has 2,3,4,7 segments
    res = 0
    for r in right:
        if len(r) in [2, 3, 4, 7]:
            res += 1
    return res


def count_part2(left, right):
    # try to assign digits
    D = {}
    d235 = []
    d069 = []
    for l in left:
        if len(l) == 2:
            # only 1 has 2 segments
            D[1] = l
        elif len(l) == 3:
            # only 7 has 3 segments
            D[7] = l
        elif len(l) == 4:
            # only 4 has 4 segments
            D[4] = l
        elif len(l) == 5:
            # 2,3,5 has 5 segments
            d235.append(l)
        elif len(l) == 6:
            # 0,6,9 has 6 segments
            d069.append(l)
        elif len(l) == 7:
            # only 8 has 7 segments
            D[8] = l

    # print("d069", d069)
    # print("d235", d235)

    for d in d069:
        if len(set(d) & set(D[1])) == 1:
            # 6 and 1 overlaps in 1 segment
            D[6] = d
        elif len(set(d) & set(D[4])) == 3:
            # 0 and 4 overlaps in 3 segments
            D[0] = d
        elif len(set(d) & set(D[4])) == 4:
            # 9 and 4 overlaps in 4 segments
            D[9] = d

    assert(D[0] is not None and D[6] is not None and D[9] is not None)

    for d in d235:
        if len(set(d) & set(D[6])) == 5:
            # 5 and 6 overlaps in 5 segments
            D[5] = d
        elif len(set(d) & set(D[1])) == 2:
            # 3 and 1 overlaps in 2 segments
            D[3] = d
        else:
            # 2 is what left
            D[2] = d

    assert(D[2] is not None and D[3] is not None and D[5] is not None)

    # print(D)

    # decode
    s = ""
    for r in right:
        for k, v in D.items():
            if set(v) == set(r):
                s += str(k)

    # print(s)
    return int(s)


def solve(lines, count_fun):
    res = 0
    for line in lines:
        line = line.strip()
        words = line.split(" | ")
        left = words[0].split(" ")
        right = words[1].split(" ")
        res += count_fun(left, right)
    return res


print(solve(lines, count_part1))  # 349
print(solve(lines, count_part2))  # 1070957

stop = datetime.now()
print("duration:", stop - start)

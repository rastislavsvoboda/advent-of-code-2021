from datetime import datetime

# pypy3.exe .\save.py 20

start = datetime.now()
lines = open('20.in').readlines()

# !! not working with sample, it has first bit '.' and puzzle input has '#'
# lines = open('20.ex1').readlines()


def step(data, algorithm, is_on):
    new_data = set()

    rows = [r for (r, c) in data]
    cols = [c for (r, c) in data]

    r1 = min(rows)
    r2 = max(rows)
    c1 = min(cols)
    c2 = max(cols)

    for r in range(r1-1, r2+2):
        for c in range(c1-1, c2+2):
            val = ""
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if is_on:
                        val += "1" if (r+dr, c+dc) in data else "0"
                    else:
                        val += "0" if (r+dr, c+dc) in data else "1"

            transform = algorithm[int(val, 2)]

            if is_on:
                # currently storing on values ("#")
                # so fo next step we need to store '.'
                if transform == '.':
                    new_data.add((r, c))
            else:
                # currently storing off values (".")
                # so fo next step we need to store '#'
                if transform == '#':
                    new_data.add((r, c))

    return new_data


def solve(lines, steps):
    algorithm = lines[0].strip()
    assert len(algorithm) == 512

    G = set()
    for r, line in enumerate(lines[2:]):
        # assert line
        for c, char in enumerate(line.strip()):
            if char == '#':
                G.add((r, c))

    for s in range(steps):
        is_on = s % 2 == 0
        G = step(G, algorithm, is_on)

    # print(G)
    return len(G)


print(solve(lines, 2))  # 5326
print(solve(lines, 50))  # 17096

stop = datetime.now()
print("duration:", stop - start)

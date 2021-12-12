from datetime import datetime
from collections import defaultdict, deque

# pypy3.exe .\save.py 12

start = datetime.now()
lines = open('12.in').readlines()
# lines = open('12.ex1').readlines()
# lines = open('12.ex2').readlines()
# lines = open('12.ex3').readlines()


def recurse(path, graph, part, paths):
    node = path[-1]
    for v in graph[node]:
        if v == 'start':
            # don't return to 'start'
            continue
        elif v == 'end':
            # 'end' reached
            paths.append(path + [v])
            continue
        elif v.isupper():
            recurse(path + [v], graph, part, paths)
        else:
            assert(v.islower())
            if v not in path:
                recurse(path + [v], graph, part, paths)
            elif part == 2:
                # for part 2 can visit a single small cave twice
                # count numbers of visits for small caves
                small_counts = defaultdict(int)
                for x in path:
                    if x.islower() and not (x == 'start' or x == 'end'):
                        small_counts[x] += 1
                if max(small_counts.values()) == 1:
                    # each small cave was visited max once
                    # can add this single small twice
                    recurse(path + [v], graph, part, paths)


def solve(lines, part):
    E = defaultdict(set)
    for line in lines:
        u, v = line.strip().split('-')
        E[u].add(v)
        E[v].add(u)

    paths = []
    recurse(['start'], E, part, paths)
    return len(paths)


print(solve(lines, 1))  # 4707
print(solve(lines, 2))  # 130493

stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
import copy

# pypy3.exe .\save.py 25

start = datetime.now()
lines = open('25.in').readlines()
# lines = open('25.ex1').readlines()
# lines = open('25.ex2').readlines()


def print_g(G):
    for row in G:
        print(''.join(row))


def solve1(lines):
    G = []
    for line in lines:
        G.append([c for c in line.strip()])

    R = len(G)
    C = len(G[0])
    # print(G)
    # print_g(G)

    step = 0
    while True:
        step += 1
        # print("after ", step)

        moved = False
        
        # first try to move any >
        G_next = copy.deepcopy(G)
        for r in range(R):
            for c in range(C):
                if G[r][c] == '>' and G[r][(c+1) % C] == '.':
                    G_next[r][(c+1) % C] = '>'
                    G_next[r][c] = '.'
                    moved = True
        G = G_next

        # next try to move any v
        G_next = copy.deepcopy(G)
        for r in range(R):
            for c in range(C):
                if G[r][c] == 'v' and G[(r+1) % R][c] == '.':
                    G_next[(r+1) % R][c] = 'v'
                    G_next[r][c] = '.'
                    moved = True
        G = G_next

        if not moved:
            break

    return step


print(solve1(lines))  # 308

stop = datetime.now()
print("duration:", stop - start)

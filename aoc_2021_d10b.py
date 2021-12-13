from datetime import datetime
from collections import deque


# pypy3.exe .\save.py 10

start = datetime.now()
lines = open('10.in').readlines()
# lines = open('10.ex1').readlines()


def solve(lines):
    OPENINGS = ['(', '[', '{', '<']
    PAIRS = {')': '(', ']': '[', '}': '{', '>': '<' }
    POINTS1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    POINTS2 = {'(': 1, '[': 2, '{': 3, '<': 4}
    corrupted_scores = []
    incomplete_scores = []
    for line in lines:
        line = line.strip()
        Q = deque()
        corrupted = False
        for x in line:
            if x in OPENINGS:
                Q.append(x)
            else:
                if Q.pop() != PAIRS[x]:
                    corrupted = True
                    break
        if corrupted:
            corrupted_scores.append(POINTS1[x])
        else:
            score = 0
            for x in reversed(Q):
                score = score * 5 + POINTS2[x]
            incomplete_scores.append(score)


    # print(corrupted_scores)
    res1 = sum(corrupted_scores)
    
    # print(incomplete_scores)
    incomplete_scores.sort()
    res2 = incomplete_scores[len(incomplete_scores) // 2]

    return res1, res2


print(solve(lines))  # 290691, 2768166558

stop = datetime.now()
print("duration:", stop - start)

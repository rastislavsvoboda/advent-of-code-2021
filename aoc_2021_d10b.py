from datetime import datetime
from collections import deque


# pypy3.exe .\save.py 10

start = datetime.now()
lines = open('10.in').readlines()
# lines = open('10.in0').readlines()


def solve(lines):
    POINTS1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    # use opposite characters
    POINTS2 = {'(': 1, '[': 2, '{': 3, '<': 4}
    corrupted_scores = []
    incomplete_scores = []
    for line in lines:
        line = line.strip()
        Q = deque()
        corrupted = False
        for c in line:
            if c in ['[', '<', '(', '{']:
                Q.append(c)
            else:
                p = Q.pop()
                if p == '[' and c != ']':
                    corrupted = True
                elif p == '<' and c != '>':
                    corrupted = True
                elif p == '(' and c != ')':
                    corrupted = True
                elif p == '{' and c != '}':
                    corrupted = True
            if corrupted:
                corrupted_scores.append(POINTS1[c])
                break
        
        if not corrupted:
            score = 0
            for c in reversed(Q):
                score = score * 5 + POINTS2[c]
            incomplete_scores.append(score)


    # print(corrupted_scorescorrupted_scores)
    res1 = sum(corrupted_scores)
    
    # print(incomplete_scores)
    incomplete_scores.sort()
    res2 = incomplete_scores[len(incomplete_scores) // 2]

    return res1, res2


print(solve(lines))  # 290691, 2768166558

stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
from collections import deque


# pypy3.exe .\save.py 10

start = datetime.now()
lines = open('10.in').readlines()
# lines = open('10.in0').readlines()


def solve(lines):
    res1 = 0
    POINTS1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    incomplete = []
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
                res1 += POINTS1[c]
                break
        
        if not corrupted:
            missing = deque()
            for c in Q:
                if c == "(":
                    missing.appendleft(')')
                if c == "[":
                    missing.appendleft(']')
                if c == "{":
                    missing.appendleft('}')
                if c == "<":
                    missing.appendleft('>')
            incomplete.append(missing)

    POINTS2 = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for q in incomplete:
        score = 0
        for x in q:
            score *= 5
            score += POINTS2[x]
        scores.append(score)

    # print(scores)
    scores.sort()
    res2 = scores[len(scores) // 2]
    return res1, res2


print(solve(lines))  # 290691, 2768166558

stop = datetime.now()
print("duration:", stop - start)

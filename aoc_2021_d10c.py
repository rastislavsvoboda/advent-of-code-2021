from datetime import datetime
from collections import deque


# pypy3.exe .\save.py 10

start = datetime.now()
lines = open('10.in').readlines()
# lines = open('10.in0').readlines()


def parse(line):
    return [x for x in line.strip()]


def is_corrupted(brackets):
    OPENINGS = '({[<'
    CLOSINGS = ')}]>'
    stack = deque()
    for b in brackets:
        if b in OPENINGS:
            stack.append(b)
        else:
            top = stack.pop()
            if OPENINGS.index(top) != CLOSINGS.index(b):
                return True, list(stack), b
    return False, list(stack), None


def score1(entry):
    POINTS1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    _corrupted, _rest, illegal = entry
    return POINTS1[illegal]


def score2(entry):
    _corrupted, rest, _illegal = entry
    POINTS2 = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for x in reversed(rest):
        score *= 5
        score += POINTS2[x]
    return score


def median(lst: list):
    sorted_lst = sorted(lst)
    return sorted_lst[len(sorted_lst) // 2]


# prepate
brackets = map(parse, lines)
data = list(map(is_corrupted, brackets))

# Part 1
corrupted = filter(lambda x: x[0] == True, data)
scores1 = map(score1, corrupted)
result1 = sum(scores1)
print(result1)  # 290691

# Part 2
incomplete = filter(lambda x: x[0] == False, data)
scores2 = map(score2, incomplete)
result2 = median(list(scores2))
print(result2)  # 2768166558


stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
from collections import deque


# pypy3.exe .\save.py 10

start = datetime.now()
lines = open('10.in').readlines()
# lines = open('10.ex1').readlines()


def parse(line):
    return [x for x in line.strip()]

# returns (True if is corrupted, rest of stack, first illegal char)
#         (False if incomplete, rest of stack, None)
def classify(brackets):
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
    _is_corrupted, _rest, illegal_char = entry
    return POINTS1[illegal_char]


def score2(entry):
    _is_corrupted, rest, _illegal_char = entry
    POINTS2 = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for x in reversed(rest):
        score *= 5
        score += POINTS2[x]
    return score


def median(lst: list):
    sorted_lst = sorted(lst)
    return sorted_lst[len(sorted_lst) // 2]


data = list(map(lambda line: classify(parse(line)), lines))
corrupted = filter(lambda x: x[0] == True, data)
print(sum(map(score1, corrupted)))
incomplete = filter(lambda x: x[0] == False, data)
print(median(map(score2, incomplete)))


stop = datetime.now()
print("duration:", stop - start)

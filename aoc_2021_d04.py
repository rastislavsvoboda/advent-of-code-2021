from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 4

start = datetime.now()
text = open('4.in').read()
# text = open('4.in0').read()


def get_data(text):
    nums = []
    data = []
    first = True
    for grp in text.split('\n\n'):
        if first:
            nums = grp.split(',')
            first = False
        else:
            entries = []
            for row in grp.split('\n'):
                entries.append(row)
            data.append(parse_entry(entries))
    return nums, data


def parse_entry(entries):
    answers = []
    for entry in entries:
        nums = re.findall(r"\d+", entry.strip())
        answers.append(nums)
    return answers


def mark(n, m, bingo):
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == n:
                m[(r, c)] = True


def check(M):
    winners = []

    for i, m in enumerate(M):
        for r in range(5):
            cnt = 0
            for c in range(5):
                if (r, c) in m:
                    cnt += 1
            if cnt == 5:
                if i not in winners:
                    winners.append(i)

        for c in range(5):
            cnt = 0
            for r in range(5):
                if (r, c) in m:
                    cnt += 1
            if cnt == 5:
                if i not in winners:
                    winners.append(i)

    return winners


def sum_unmarked(mark, bingo):
    sum = 0
    for r in range(5):
        for c in range(5):
            if (r, c) not in mark:
                sum += int(bingo[r][c])
    return sum


def solve(text, part):
    nums, data = get_data(text)
    # print(nums)

    # matches for boards
    M = []
    for i in range(len(data)):
        M.append({})

    order = []
    for n in nums:
        for i, d in enumerate(data):
            mark(n, M[i], d)
        winners = check(M)
        for w in winners:
            if w not in order:
                order.append(w)

        if part == 1:
            # until first winner
            if len(order) == 1:
                break
        else:
            # until all winners
            if len(order) == len(M):
                break

    # print("order of winners", order)
    board_index = order[-1]
    sum = sum_unmarked(M[board_index], data[board_index])
    # print("sum of all unmarked numbers", sum)
    # print("the number that was just called", n)
    return sum * int(n)


print(solve(text, 1))  # 23177
print(solve(text, 2))  # 6804

stop = datetime.now()
print("duration:", stop - start)

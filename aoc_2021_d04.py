from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 4

start = datetime.now()
lines = open('4.in').readlines()
lines = open('4.in0').readlines()
# text = open('4.in').read()


# def get_data(text):
#     data = []
#     for grp in text.split('\n\n'):
#         entries = []
#         for row in grp.split():
#             entries.append(row)
#         data.append(parse_entry(entries))
#     return data

# def parse_entry(entries):
#     # answers = []
#     # for entry in entries:
#     #     answers.append(set(entry))
#     # return answers
#     return entries

def solve1(lines):
    res = 0

    for line in lines:
        line = line.strip()
        words = line.split()
        nums = re.findall(r"[+-]?\d+", line)
        print(line)
        # print(words)
        # print(nums)
        
        res += 1

    return res


# def solve1_t(text):
#     res = 0
    
#     data = get_data(text)
#     for d in data:
#         print(d)
#         res += 1

#     return res


print(solve1(lines))  #
# print(solve1_t(text))  #
# print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)
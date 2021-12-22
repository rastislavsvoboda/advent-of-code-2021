from datetime import datetime
from collections import defaultdict, deque, Counter
import copy
import re

# pypy3.exe .\save.py 22

start = datetime.now()
lines = open('22.in').readlines()
# lines = open('22.ex1').readlines()
# lines = open('22.ex2').readlines()
lines = open('22.ex3').readlines()


# text = open('22.in').read()


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

    G=set()
    for line in lines:
        line = line.strip()
        words = line.split()
        nums= [int(v) for v in re.findall(r"[+-]?\d+", line)]
        x1,x2,y1,y2,z1,z2 = nums
        
        to_on = True if line.startswith('on') else False
        # print(line)
        # print(to_on,x1,x2,y1,y2,z1,z2)

        if x1 < -50:
            x1 = 50
        if x2 > 50:
            x2 = -50

        if y1 < -50:
            y1 = 50
        if y2 > 50:
            y2 = -50            

        if z1 < -50:
            z1 = 50
        if z2 > 50:
            z2 = -50            

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    if to_on:
                        G.add((x,y,z))
                    else:
                        if (x,y,z) in G:
                            G.remove((x,y,z))                


        # print(line)
        # print(words)
        # print(nums)
        
        res = len(G)

    return res


# def solve1_t(text):
#     res = 0
    
#     data = get_data(text)
#     for d in data:
#         print(d)
#         res += 1

#     return res


print(solve1(lines))  # 545118
# print(solve1_t(text))  #
# print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)
from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque
import copy
import re
import time

# pypy3.exe .\save.py 3

start = datetime.now()
lines = open('3.in').readlines()
# lines = open('3.in0').readlines()


def solve1(lines):
    res = 0
    # 110011110101
    G0=[0,0,0,0,0,0,0,0,0,0,0,0]
    G1=[0,0,0,0,0,0,0,0,0,0,0,0]
    for line in lines:
        line = line.strip()
        # words = line.split()
        # nums = re.findall(r"[+-]?\d+", line)
        # print(line)
        for i in range(len(line)):
            # print(line[i])
            if line[i] == '0':
                G0[i] += 1
            elif line[i] == '1':
                G1[i] += 1
            else:
                print('error')


    print(G0)
    print(G1)

    n1 = ""
    n2 = "" 
    for i in range(len(G0)):
        if G0[i] > G1[i]:
            n1 += '0'
            n2 += '1'
        else:
            n1 += '1'
            n2 += '0'

    print(n1, n2)
        

    b1= int(n1, 2)
    b2= int(n2, 2)

    print(b1, b2)
        
    return b1* b2




def arr(lines):
    A=[]
    for line in lines:
        line = line.strip()
        a = []
        for c in line:
            if c=='0':
                a.append(0)
            else:
                a.append(1)
        A.append(a)
    return A


def count_nums(data, i):

    n1 = 0
    n0 = 0
    for r in data:
        if r[i] == 1:
            n1 += 1
        else:
            n0 += 1

    return (n0,n1)
        



def solve2(lines):

    x = arr(lines)
    print(x)     
    print("--")

    val1 = ""

    i = 0
    while i < len(x[0]):

        n0,n1 = count_nums(x,i)
        print(n0,n1)
        if n1 >= n0:
            x = list(filter(lambda r: r[i] == 1, x))
            val1 += '1'
        else:
            x = list(filter(lambda r: r[i] == 0, x))
            val1 += '0'

        print(x)
        print("--")
        i+=1

    val1d = int(val1, 2)
    print(val1, val1d)


    x = arr(lines)
    print(x)     

    i = 0
    while len(x) != 1:

        n0,n1 = count_nums(x,i)
        print(n0,n1)
        if n1 >= n0:
            x = list(filter(lambda r: r[i] == 0, x))
        else:
            x = list(filter(lambda r: r[i] == 1, x))

        print(x)
        print("--")
        i+=1

    print(x)

    val2 = ""
    for c in x[0]:
        if c == 0:
            val2 += '0'
        else:
            val2 += '1'


    val2d = int(val2, 2)
    print(val2, val2d)






    return val1d * val2d


# print(solve1(lines))  #
print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)
from datetime import datetime

# pypy3.exe .\save.py 1

start = datetime.now()
lines = open('1.in').readlines()


def data1(xs):
    for i in range(len(xs)):
        if i >= 1:
            yield (xs[i-1], xs[i])


def data2(xs):
    for i in range(len(xs)):
        if i >= 3:
            yield (xs[i-1]+xs[i-2]+xs[i-3], xs[i]+xs[i-1]+xs[i-2])


def solve(data):
    res = 0

    for (a, b) in data:
        if b > a:
            res += 1

    return res


numbers = [int(line) for line in lines]
print(solve(data1(numbers)))  # 1393
print(solve(data2(numbers)))  # 1359


stop = datetime.now()
print("duration:", stop - start)

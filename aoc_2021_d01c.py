from datetime import datetime

# pypy3.exe .\save.py 1

start = datetime.now()
lines = open('1.in').readlines()
# lines = open('1.ex1').readlines()


def count_increases(data):
    return sum(a < b for (a, b) in zip(data, data[1:]))


def solve1(data):
    return count_increases(data)


def solve2(data):
    triples = zip(data, data[1:], data[2:])
    sums = list(map(lambda triple: sum(triple), triples))
    return count_increases(sums)


numbers = [int(line) for line in lines]
print(solve1(numbers))  # 1393
print(solve2(numbers))  # 1359


stop = datetime.now()
print("duration:", stop - start)

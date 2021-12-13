from datetime import datetime

# pypy3.exe .\save.py 1

start = datetime.now()
lines = open('1.in').readlines()
# lines = open('1.ex1').readlines()


def solve1(data):
    return sum(a < b for (a, b) in zip(data, data[3:]))
    # return len(list(filter(lambda pair: pair[0] < pair[1], zip(data, data[1:]))))


def solve2(data):
    return sum(a < b for (a, b) in zip(data, data[3:]))
    # return sum(1 for (a, b) in zip(data, data[3:]) if a < b)

numbers = [int(line) for line in lines]
print(solve1(numbers))  # 1393
print(solve2(numbers))  # 1359


stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
from datetime import timedelta
from collections import defaultdict, deque

# pypy3.exe .\save.py 3

start = datetime.now()
lines = open('3.in').readlines()
# lines = open('3.in0').readlines()


def arr_of_bits(lines):
    A = []
    for line in lines:
        line = line.strip()
        bits = []
        for c in line:
            if c == '0':
                bits.append(0)
            else:
                bits.append(1)
        A.append(bits)
    return A


def count_nums(data, i):
    num0 = 0
    num1 = 0
    for r in data:
        if r[i] == 1:
            num1 += 1
        else:
            num0 += 1

    return (num0, num1)


def bits_to_decimal(bits):
    res = 0
    length = len(bits)
    for i in range(length):
        res += bits[length-1-i] * 2**i
    return res


def solve1(lines):
    data = arr_of_bits(lines)
    length = len(data[0])
    gama = []
    epsilon = []

    for i in range(length):
        num0, num1 = count_nums(data, i)
        if num1 >= num0:
            gama.append(1)
            epsilon.append(0)
        else:
            gama.append(0)
            epsilon.append(1)

    gama_rate = bits_to_decimal(gama)
    # print ("gama_rate", gama_rate)

    epsilon_rate = bits_to_decimal(epsilon)
    # print ("epsilon_rate", epsilon_rate)

    return gama_rate * epsilon_rate



def solve2(lines):
    data = arr_of_bits(lines)
    i = 0
    while len(data) != 1:
        n0, n1 = count_nums(data, i)
        # print(n0,n1)
        if n1 >= n0:
            data = list(filter(lambda r: r[i] == 1, data))
        else:
            data = list(filter(lambda r: r[i] == 0, data))

        i += 1

    oxygen_rating = bits_to_decimal(data[0])
    # print("oxygen generator rating", oxygen_rating)

    data = arr_of_bits(lines)
    i = 0
    while len(data) != 1:

        n0, n1 = count_nums(data, i)
        # print(n0,n1)
        if n1 >= n0:
            data = list(filter(lambda r: r[i] == 0, data))
        else:
            data = list(filter(lambda r: r[i] == 1, data))

        i += 1

    co2_rating = bits_to_decimal(data[0])
    # print("CO2 scrubber rating", co2_rating)

    return oxygen_rating * co2_rating


print(solve1(lines))  # 2967914
print(solve2(lines))  # 7041258

stop = datetime.now()
print("duration:", stop - start)

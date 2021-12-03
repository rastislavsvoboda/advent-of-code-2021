from datetime import datetime

# pypy3.exe .\save.py 3

start = datetime.now()
lines = open('3.in').readlines()
# lines = open('3.in0').readlines()


# count number of zeros and ones on i-th position
def count_nums(data, index):
    n0, n1 = 0, 0

    for line in data:
        line = line.strip()
        if line[index] == '1':
            n1 += 1
        else:
            n0 += 1

    return (n0, n1)


def solve1(lines):
    data = lines
    length = len(data[0].strip())
    # print(length)

    gama = ""
    epsilon = ""

    for i in range(length):
        # print(i)
        n0, n1 = count_nums(data, i)

        if n1 > n0:
            gama += '1'
            epsilon += '0'
        elif n0 > n1:
            gama += '0'
            epsilon += '1'
        else:
            assert "wrong data - tie"

    gama_rate = int(gama, 2)
    # print("gama_rate", gama_rate)

    epsilon_rate = int(epsilon, 2)
    # print("epsilon_rate", epsilon_rate)

    return gama_rate * epsilon_rate


def solve2(lines):
    data = lines
    i = 0
    while len(data) > 1:
        n0, n1 = count_nums(data, i)
        # print(n0, n1)
        if n1 >= n0:
            data = [x for x in data if x[i] == '1']
        else:
            data = [x for x in data if x[i] == '0']

        i += 1

    oxygen_rating = int(data[0], 2)
    # print("oxygen generator rating", oxygen_rating)

    data = lines
    i = 0
    while len(data) > 1:
        n0, n1 = count_nums(data, i)
        # print(n0,n1)
        if n1 >= n0:
            data = [x for x in data if x[i] == '0']
        else:
            data = [x for x in data if x[i] == '1']

        i += 1

    co2_rating = int(data[0], 2)
    # print("CO2 scrubber rating", co2_rating)

    return oxygen_rating * co2_rating


print(solve1(lines))  # 2967914
print(solve2(lines))  # 7041258

stop = datetime.now()
print("duration:", stop - start)

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

    gamma = ""
    epsilon = ""

    for i in range(length):
        # print(i)
        n0, n1 = count_nums(data, i)

        if n1 > n0:
            gamma += '1'
            epsilon += '0'
        elif n0 > n1:
            gamma += '0'
            epsilon += '1'
        else:
            assert "wrong data - tie"

    gamma_rate = int(gamma, 2)
    # print("gamma_rate", gamma_rate)

    epsilon_rate = int(epsilon, 2)
    # print("epsilon_rate", epsilon_rate)

    return gamma_rate * epsilon_rate


def solve2(lines):
    data = lines
    length = len(data[0].strip())
    # print(length)

    oxygen = data
    co2 = data

    for i in range(length):
        if len(oxygen) > 1:
            n0, n1 = count_nums(oxygen, i)
            # print(n0, n1)
            if n1 >= n0:
                oxygen = [x for x in oxygen if x[i] == '1']
            else:
                oxygen = [x for x in oxygen if x[i] == '0']

        if len(co2) > 1:
            n0, n1 = count_nums(co2, i)
            # print(n0,n1)
            if n1 >= n0:
                co2 = [x for x in co2 if x[i] == '0']
            else:
                co2 = [x for x in co2 if x[i] == '1']

    oxygen_rating = int(oxygen[0], 2)
    # print("oxygen generator rating", oxygen_rating)

    co2_rating = int(co2[0], 2)
    # print("CO2 scrubber rating", co2_rating)

    return oxygen_rating * co2_rating


print(solve1(lines))  # 2967914
print(solve2(lines))  # 7041258

stop = datetime.now()
print("duration:", stop - start)

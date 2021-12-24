from datetime import datetime
from itertools import product

# pypy3.exe .\save.py 24

start = datetime.now()
lines = open('24.in').readlines()


# row 6: like add x 13 or add x -5
X = [13, 11, 15, -11, 14, 0, 12, 12, 14, -6, -10, -12, -3, -5]

# row 16: like add y 13 or add y 9
Y = [13, 10, 5, 14, 5, 15, 4, 11, 1, 15, 12, 8, 14, 9]

# row 5: div z 1 or div z 26
Z = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]

# there are 7 values where Z is 26 and where 1


def is_valid(digits):
    z = 0
    res = [0] * 14

    digits_idx = 0

    for i in range(14):
        add_x = X[i]
        add_y = Y[i]
        div_z = Z[i]

        if div_z == 26:
            res[i] = ((z % 26) + add_x)
            z //= 26
            if not (1 <= res[i] <= 9):
                return False

        else:
            z = z * 26 + digits[digits_idx] + add_y
            res[i] = digits[digits_idx]
            digits_idx += 1

    return res


def solve(part):
    if part == 1:
        # decreasing from 9999999
        input_space = product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=7)
    else:
        # increasing from 1111111
        input_space = product([1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=7)

    for digits in input_space:
        res = is_valid(digits)
        if res:
            break

    code = "".join([str(i) for i in res])
    return code


print(solve(1))  # 12934998949199
print(solve(2))  # 11711691612189

stop = datetime.now()
print("duration:", stop - start)

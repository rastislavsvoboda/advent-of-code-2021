from datetime import datetime
from itertools import product

# pypy3.exe .\save.py 24

start = datetime.now()
lines = open('24.in').readlines()


# program is basically 14 blocks of the "same" instructions
# varying on rows:

# row 6: like add x 13 or add x -5
X = [13, 11, 15, -11, 14, 0, 12, 12, 14, -6, -10, -12, -3, -5]

# row 16: like add y 13 or add y 9
Y = [13, 10, 5, 14, 5, 15, 4, 11, 1, 15, 12, 8, 14, 9]

# row 5: div z 1 or div z 26
Z = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]

# only z reg is relevant between "independent" blocks
# out of 14 values there are 7 values where Z is 26 and where 1
# "relevant" are these where 26
# we don't need to brute force 9**14 which is impossible
# but only 9**7

def is_valid(digits):
    # reduced algorithm
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


def run(program, input):
    # original program interpretter
    regs = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    pc = 0
    input_idx = 0

    while pc < len(program):
        if len(program[pc]) == 2:
            cmd, a = program[pc]
            assert cmd == "inp"
            assert input_idx < len(input)
            regs[a] = input[input_idx]
            input_idx += 1
        else:
            assert len(program[pc]) == 3
            cmd, a, reg_or_int = program[pc]
            b = regs[reg_or_int] if reg_or_int in regs else int(reg_or_int)

            if cmd == "add":
                regs[a] += b
            elif cmd == "mul":
                regs[a] *= b
            elif cmd == "div":
                assert b != 0
                regs[a] //= b
            elif cmd == "mod":
                assert regs[a] >= 0
                assert b > 0
                regs[a] %= b
            elif cmd == "eql":
                regs[a] = 1 if regs[a] == b else 0
            else:
                assert False
        pc += 1

    return regs['z'] == 0


def solve(lines, part):
    instructions = [line.strip().split() for line in lines]
    # 0 not allowed
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if part == 1:
        # decreasing from 9999999
        input_space = product(reversed(digits), repeat=7)
    else:
        # increasing from 1111111
        input_space = product(digits, repeat=7)

    for digits in input_space:
        res = is_valid(digits)
        if res:
            break

    assert run(instructions, res)

    code = "".join([str(i) for i in res])

    return code


print(solve(lines, 1))  # 12934998949199
print(solve(lines, 2))  # 11711691612189

stop = datetime.now()
print("duration:", stop - start)

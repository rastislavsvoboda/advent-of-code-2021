from datetime import datetime

# pypy3.exe .\save.py 2

start = datetime.now()
lines = open('2.in').readlines()
# lines = open('2.ex1').readlines()


def solve1(lines):
    h_pos = 0 # horizontal position  
    depth = 0
    for line in lines:
        words = line.strip().split()
        cmd = words[0]
        x = int(words[1])

        if cmd == 'down':
            depth += x
        elif cmd == 'up':
            depth -= x
        elif cmd == 'forward':
            h_pos += x
        else:
            print('error')

    # print(h_pos, depth)
    return h_pos * depth


def solve2(lines):
    h_pos = 0 # horizontal pos
    depth = 0
    aim = 0
    for line in lines:
        words = line.strip().split()
        cmd = words[0]
        x = int(words[1])

        if cmd == 'down':
            aim += x
        elif cmd == 'up':
            aim -= x
        elif cmd == 'forward':
            h_pos += x
            depth += aim * x
        else:
            print('error')

    # print(h_pos, depth)
    return h_pos * depth


print(solve1(lines))  # 1488669
print(solve2(lines))  # 1176514794

stop = datetime.now()
print("duration:", stop - start)

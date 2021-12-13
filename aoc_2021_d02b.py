from datetime import datetime
from collections import namedtuple
from functools import reduce

# pypy3.exe .\save.py 2

start = datetime.now()
lines = open('2.in').readlines()
# lines = open('2.ex1').readlines()

Entry = namedtuple('Entry', 'command units')
State1 = namedtuple('State1', 'h_pos depth')
State2 = namedtuple('State2', 'h_pos depth aim')


def parse(line):
    # command units
    # down 5
    # forward 8
    # up 3
    words = line.strip().split()
    return Entry(words[0], int(words[1]))


def compute_part1(state: State1, entry: Entry):
    if entry.command == 'down':
        return State1(state.h_pos, state.depth + entry.units)
    if entry.command == 'up':
        return State1(state.h_pos, state.depth - entry.units)
    if entry.command == 'forward':
        return State1(state.h_pos + entry.units, state.depth)
    assert False, "Invalid command: " + entry.command


def solve1(lines):
    entries = map(parse, lines)
    result = reduce(compute_part1, entries, State1(0, 0))
    # print(result)
    return result.h_pos * result.depth


def compute_part2(state: State2, entry: Entry):
    if entry.command == 'down':
        return State2(state.h_pos, state.depth, state.aim + entry.units)
    if entry.command == 'up':
        return State2(state.h_pos, state.depth, state.aim - entry.units)
    if entry.command == 'forward':
        return State2(state.h_pos + entry.units, state.depth + state.aim * entry.units, state.aim)
    assert False, "Invalid command: " + entry.command


def solve2(lines):
    entries = map(parse, lines)
    result = reduce(compute_part2, entries, State2(0, 0, 0))
    # print(result)
    return result.h_pos * result.depth


print(solve1(lines))  # 1488669
print(solve2(lines))  # 1176514794

stop = datetime.now()
print("duration:", stop - start)

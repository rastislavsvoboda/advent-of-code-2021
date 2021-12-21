from datetime import datetime
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations, repeat

# pypy3.exe .\save.py 21

start = datetime.now()
lines = open('21.in').readlines()
# lines = open('21.ex1').readlines()


def dice_generator():
    d = 0
    # internally from 0-99, but returns 1-100
    while True:
        yield (d+1)
        d = (d+1) % 100


def next_position(current, advance):
    return ((current-1+advance) % 10)+1


def solve1(lines):
    p1 = int(lines[0].strip().split(':')[1].strip())
    p2 = int(lines[1].strip().split(':')[1].strip())

    POS = [p1, p2]
    SCORE = [0, 0]
    player = 0
    dice = dice_generator()
    dice_rolled = 0

    while True:
        dices = [next(dice) for _ in range(3)]
        dice_rolled += len(dices)
        rolled_val = sum(dices)

        POS[player] = next_position(POS[player], rolled_val)
        SCORE[player] += POS[player]

        if SCORE[player] >= 1000:
            break

        player = (player+1) % 2

    loosing_player = (player+1) % 2

    return SCORE[loosing_player] * dice_rolled



def solve2(lines):
    return None


print(solve1(lines))  # 913560
# print(solve2(lines))  #

stop = datetime.now()
print("duration:", stop - start)

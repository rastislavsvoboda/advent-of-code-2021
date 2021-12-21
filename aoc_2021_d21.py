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


def next_player(current):
    return (current+1) % 2


def solve1(lines):
    p1 = int(lines[0].strip().split(':')[1].strip())
    p2 = int(lines[1].strip().split(':')[1].strip())

    POS = [p1, p2]
    SCORE = [0, 0]
    player = 0
    dice = dice_generator()
    dice_rolled_count = 0

    while True:
        dices = [next(dice) for _ in range(3)]
        dice_rolled_count += len(dices)
        rolled_val = sum(dices)

        POS[player] = next_position(POS[player], rolled_val)
        SCORE[player] += POS[player]

        if SCORE[player] >= 1000:
            # player win
            break

        player = next_player(player)

    loosing_player = next_player(player)

    return SCORE[loosing_player] * dice_rolled_count


# idea based on Jonathan Paulson
def play(pos1, pos2, score1, score2, memo=None):
    if memo is None:
        memo = {}
    if score1 >= 21:
        return (1, 0)
    if score2 >= 21:
        return (0, 1)

    if (pos1, pos2, score1, score2) in memo:
        return memo[(pos1, pos2, score1, score2)]

    res = (0, 0)
    # for  in repeat([1,2,3],3):

    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                rolled_val = d1+d2+d3
                next_pos1 = next_position(pos1, rolled_val)
                next_score1 = score1 + next_pos1
                next_res = play(pos2, next_pos1, score2, next_score1, memo)
                res = (res[0]+next_res[1], res[1]+next_res[0])

    memo[(pos1, pos2, score1, score2)] = res
    return res


def solve2(lines):
    p1 = int(lines[0].strip().split(':')[1].strip())
    p2 = int(lines[1].strip().split(':')[1].strip())

    stats = play(p1, p2, 0, 0)
    wins = max(stats)
    looses = min(stats)
    # print("wins:", wins, "looses:", looses)
    return wins


print(solve1(lines))  # 913560
print(solve2(lines))  # 110271560863819

stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime

# pypy3.exe .\save.py 21

start = datetime.now()
lines = open('21.in').readlines()
# lines = open('21.ex1').readlines()


def parse(line):
    return int(line.strip().split(':')[1].strip())


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
    p1 = parse(lines[0])
    p2 = parse(lines[1])

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
            # player wins
            break

        player = next_player(player)

    loosing_player = next_player(player)

    return SCORE[loosing_player] * dice_rolled_count


def play(player, pos1, pos2, score1, score2, memo=None):
    if memo is None:
        memo = {}

    if score1 >= 21:
        return (1, 0)

    if score2 >= 21:
        return (0, 1)

    if (player, pos1, pos2, score1, score2) in memo:
        return memo[(player, pos1, pos2, score1, score2)]

    # (# of wins for player  1, # of wins for player 2)
    res = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                rolled_val = d1+d2+d3
                next_pos1 = next_position(pos1, rolled_val) if player == 0 else pos1
                next_score1 = score1 + next_pos1            if player == 0 else score1
                next_pos2 = next_position(pos2, rolled_val) if player == 1 else pos2
                next_score2 = score2 + next_pos2            if player == 1 else score2
                wins1, wins2 = play(next_player(player), next_pos1, next_pos2, next_score1, next_score2, memo)
                res = (res[0]+wins1, res[1]+wins2)

    memo[(player, pos1, pos2, score1, score2)] = res
    return res    


def solve2(lines):
    p1 = parse(lines[0])
    p2 = parse(lines[1])

    wins1, wins2 = play(0, p1, p2, 0, 0)

    return max(wins1, wins2)


print(solve1(lines))  # 913560
print(solve2(lines))  # 110271560863819

stop = datetime.now()
print("duration:", stop - start)

from datetime import datetime
from copy import deepcopy

# pypy3.exe .\save.py 23

start = datetime.now()
lines = open('23.in').readlines()
# lines = open('23.ex1').readlines()

# example - part1
# A = ['B', 'A']
# B = ['C', 'D']
# C = ['B', 'C']
# D = ['D', 'A']

# example - part2
# A = ['B', 'D', 'D', 'A']
# B = ['C', 'C', 'B', 'D']
# C = ['B', 'B', 'A', 'C']
# D = ['D', 'A', 'C', 'A']


EMPTY = '.'
hallway = EMPTY * 11
energies = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def all_at_home(rooms):
    for home_elm, room in rooms.items():
        for elm in room:
            if elm != home_elm:
                return False
    return True


def can_leave_room(home_elm, room):
    for elm in room:
        if elm != home_elm and elm != EMPTY:
            return True
    return False


def can_enter_home(home_elm, room):
    for elm in room:
        if elm != home_elm and elm != EMPTY:
            return False
    return True


def home_column_index(elm):
    return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[elm]


def room_leave_row_index(hallway):
    for i, e in enumerate(hallway):
        if e != EMPTY:
            return i
    return None


def room_enter_row_index(room):
    for i, e in reversed(list(enumerate(room))):
        if e == EMPTY:
            return i
    return None


def is_between(idx, home_elm, hallway_idx):
    # 0 1 2 3 4 5 6 7 8 9 10
    #     A   B   C   D
    return (home_column_index(home_elm) < idx < hallway_idx) or (hallway_idx < idx < home_column_index(home_elm))


def can_pass(bot, hallway_idx, hallway):
    for idx in range(len(hallway)):
        if is_between(idx, bot, hallway_idx) and hallway[idx] != EMPTY:
            return False
    return True


def solve(state, memo=None):
    if memo is None:
        memo = {}

    rooms, hallway = state
    key = (tuple((k, tuple(v)) for k, v in rooms.items()), tuple(hallway))

    if all_at_home(rooms):
        return 0

    if key in memo:
        return memo[key]

    for src_hallway_col_idx, elm in enumerate(hallway):
        if elm != EMPTY and can_enter_home(elm, rooms[elm]):
            if can_pass(elm, src_hallway_col_idx, hallway):
                dst_room_row_idx = room_enter_row_index(rooms[elm])
                assert dst_room_row_idx is not None
                r_dist = dst_room_row_idx + 1
                c_dist = abs(home_column_index(elm)-src_hallway_col_idx)
                distance = r_dist + c_dist
                move_energy = energies[elm] * distance
                new_hallway = list(hallway)
                new_hallway[src_hallway_col_idx] = EMPTY
                new_rooms = deepcopy(rooms)
                new_rooms[elm][dst_room_row_idx] = elm
                return move_energy + solve((new_rooms, new_hallway), memo)

    res = int(1e9)
    for home_elm, room in rooms.items():
        if not can_leave_room(home_elm, room):
            continue
        src_room_row_idx = room_leave_row_index(room)
        assert src_room_row_idx is not None
        elm = room[src_room_row_idx]
        for dest_hallway_col_idx in range(len(hallway)):
            if dest_hallway_col_idx in [2, 4, 6, 8]:
                # cannot stop above rooms
                continue
            if hallway[dest_hallway_col_idx] != EMPTY:
                continue
            if can_pass(home_elm, dest_hallway_col_idx, hallway):
                r_dist = src_room_row_idx + 1
                c_dist = abs(dest_hallway_col_idx - home_column_index(home_elm))
                distance = r_dist + c_dist
                move_energy = energies[elm] * distance
                new_hallway = list(hallway)
                assert new_hallway[dest_hallway_col_idx] == EMPTY
                new_hallway[dest_hallway_col_idx] = elm
                new_rooms = deepcopy(rooms)
                assert new_rooms[home_elm][src_room_row_idx] == elm
                new_rooms[home_elm][src_room_row_idx] = EMPTY
                new_res = move_energy + solve((new_rooms, new_hallway), memo)
                res = min(res, new_res)
    memo[key] = res
    return res


def solve1():
    A = ['C', 'C']
    B = ['B', 'D']
    C = ['A', 'A']
    D = ['D', 'B']
    hallway = EMPTY * 11
    initial_state = ({'A': A, 'B': B, 'C': C, 'D': D}, hallway)
    return solve(initial_state)


def solve2():
    A = ['C', 'D', 'D', 'C']
    B = ['B', 'C', 'B', 'D']
    C = ['A', 'B', 'A', 'A']
    D = ['D', 'A', 'C', 'B']
    hallway = EMPTY * 11
    initial_state = ({'A': A, 'B': B, 'C': C, 'D': D}, hallway)
    return solve(initial_state)


print(solve1())  # 13558
print(solve2())  # 56982

stop = datetime.now()
print("duration:", stop - start)

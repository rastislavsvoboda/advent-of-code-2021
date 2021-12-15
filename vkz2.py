from collections import deque

# koza, vlk, zeli, prevoznik na lavej strane
l = set(["K", "V", "Z", "P"])
# idu na pravu stranu
r = set()

M = {}


def to_str(side):
    res = ""
    res += "P" if "P" in side else " "
    res += "K" if "K" in side else " "
    res += "V" if "V" in side else " "
    res += "Z" if "Z" in side else " "

    return res
    # return "".join(sorted(s))


def state_to_str(state):
    l, r = state
    return to_str(l) + " | " + to_str(r)


def check(side):
    if "K" in side and "Z" in side and "P" not in side:
        # koza zozerie zeli
        return False

    if "V" in side and "K" in side and "P" not in side:
        # vlk zozerie kozu
        return False

    # vsetko ok
    return True


def is_win(state):
    l, r = state
    if l == set():
        return True
    return False


def get_options(state):
    opt = []
    l, p = state
    if "P" in l:
        # prevoznik je na lavej strane
        moving = set("P")
        opt.append((l - moving, p | moving))
        others = [x for x in l if x != "P"]
        for x in others:
            moving = set([x, "P"])
            opt.append((l - moving, p | moving))
    else:
        # prevoznik je na pravej strane
        moving = set("P")
        opt.append((l | moving, p - moving))
        others = [x for x in p if x != "P"]
        for x in others:
            moving = set([x, "P"])
            opt.append((l | moving, p - moving))

    return opt


s = (l, r)
# print(state_to_str(s))

# M[state_to_str(s)] = []

# seen = set()

Q = deque()
Q.append((s, 0, []))

wins = []


while Q:
    state, length, prev_state = Q.popleft()
    s = state_to_str(state)

    if is_win(state):
        wins.append((state, length, prev_state))

    if s in M:
        l, ps = M[s]
        if length <= l:
            if prev_state in ps:
                continue
            M[s] = (length, ps + [prev_state])
        else:
            continue
    else:
        M[s] = (length, [prev_state])

    options = get_options(state)
    for opt in options:
        l, r = opt
        if not (check(l) and check(r)):
            continue
        Q.append(((l, r), length + 1, s))


def print_path(M, s, q):
    if s == []:
        print("cesta:")
        while q:
            print(q.pop())
        print()
        return
    q.append(s)
    if s in M:
        _, prev_states = M[s]
        for p in prev_states:
            q1 = deque(q)
            print_path(M, p, q)
            q = q1

# print(M)


for (state, length, prev_state) in wins:
    # print(state)
    # print(length)
    s = state_to_str(state)
    q = deque()
    q.append(s)
    print_path(M, prev_state, q)

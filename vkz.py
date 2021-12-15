from collections import defaultdict, deque

l = set(["K", "V", "Z", "P"])
p = set()

M = {}

def to_str(s):
    return "-".join(sorted(s))


def state_to_str(state):
    l, p = state
    return to_str(l) + "|" + to_str(p)


def check(strana):
    if "K" in strana and "Z" in strana and "P" not in strana:
        return False

    if "K" in strana and "V" in strana and "P" not in strana:
        return False

    return True

def is_win(state):
    l, p = state
    if l == set() and len(p) == 4:
        return True
    return False


def gen_move(state):
    moznosti = []
    l, p = state
    if "P" in l:
        moznosti.append(((l - set("P")), (p | set("P")), "P->"))
        others = [x for x in l if x != "P"]
        for x in others:
            moznosti.append(((l - set([x, "P"])), (p | set([x, "P"])), x + "-P->"))
    else:
        moznosti.append(((l | set("P")), (p - set("P")), "<-P"))
        others = [x for x in p if x != "P"]
        for x in others:
            moznosti.append(((l | set([x, "P"]), (p - set([x, "P"])), "<-P-" + x)))

    return moznosti



s = (l, p)
# print(state_to_str(s))

# M[state_to_str(s)] = []

# seen = set()

Q = deque()
Q.append((s,[]))

wins = []


while Q:
    state, path = Q.popleft()
    s = state_to_str(state)

    if is_win(state):
        wins.append((state, path))

    if s in M:
        continue
    M[s] = path
    
    options = gen_move(state)
    for opt in options:
        l,p,m = opt
        if not (check(l) and check(p)):
            continue
        Q.append(((l,p), path + [m]))

for (state, path) in wins:
    print(state)
    print(path)
    print("---")

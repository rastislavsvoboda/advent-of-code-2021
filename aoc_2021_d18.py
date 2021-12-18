from datetime import datetime
from itertools import permutations

# pypy3.exe .\save.py 18

start = datetime.now()
lines = open('18.in').readlines()
# lines = open('18.ex1').readlines()
# lines = open('18.ex2').readlines()
# lines = open('18.ex3').readlines()
# lines = open('18.ex4').readlines()
# lines = open('18.ex5').readlines()
# lines = open('18.ex6').readlines()


class Val:
    def __init__(self, val):
        self.val = val
        self.parent = None

    def __add__(self, other):
        return self.val + other.val

    def __repr__(self):
        return str(self.val) + ' ' + str(self.parent)

    def __str__(self):
        return str(self.val)


class SN:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.parent = None
        self.l.parent = self
        self.r.parent = self

    def __repr__(self):
        return f'[{self.l},{self.r}]'


def add(n1, n2):
    return SN(n1, n2)


def split_value(x):
    if x % 2 == 0:
        return SN(Val(x//2), Val(x//2))

    return SN(Val(x//2), Val(x//2+1))


def magnitude(x):
    if type(x) == Val:
        return x.val
    if type(x) == SN:
        return 3 * magnitude(x.l) + 2 * magnitude(x.r)


def parse(str):
    if len(str) == 0:
        return None

    current = ""

    stack = []
    for x in str:
        if x == '[':
            current = ""
        elif x == ']':
            if current != "":
                stack.append(Val(int(current)))
            r = stack.pop()
            l = stack.pop()
            stack.append(SN(l, r))
            current = ""
        elif x == ',':
            if current != "":
                stack.append(Val(int(current)))
                current = ""
        else:
            current = "" + x

    res = stack.pop()
    assert len(stack) == 0
    assert res.l is not None
    assert res.r is not None
    return res


def traverse(n, level):
    if type(n) == Val:
        print(".."*level, n)
        return
    if type(n) == SN:
        traverse(n.l, level+1)
        traverse(n.r, level+1)
        return
    assert False, "unknown type"


def find_values(n, level, data):
    if type(n) == Val:
        # print(".."*level, n)
        data.append((level, n))
        return
    if type(n) == SN:
        find_values(n.l, level+1, data)
        find_values(n.r, level+1, data)
        return
    assert False, "unknown type"


def explode(root):
    # collect all values
    values = []
    find_values(root, 0, values)

    for i, v in enumerate(values):
        # print(i,v)
        level, num = v
        if level == 5:
            # found first with level 5

            found_parent = num.parent
            left = found_parent.l.val
            right = found_parent.r.val
            # print(found_parent, left, right)

            # determine which side it is
            # replace node with val 0
            parent_parent = found_parent.parent
            new_node = Val(0)
            new_node.parent = parent_parent
            # replace correct child
            if parent_parent.l == found_parent:
                parent_parent.l = new_node
            elif parent_parent.r == found_parent:
                parent_parent.r = new_node
            else:
                assert False, "child does not match left or right"

            if i >= 1:
                # it is not first, add left value to previous value
                before = values[i-1][1]
                before.val += left

            if i < len(values)-2:
                # it is not last, add right value to next value
                # very next element is child, so skip that
                after = values[i+2][1]
                after.val += right

            return True
    return False


def split(root):
    # collect all values
    values = []
    find_values(root, 0, values)

    for i, v in enumerate(values):
        # print(i,v)
        _level, num = v

        if num.val >= 10:
            # found first 10 or greater

            # split value
            found_parent = num.parent
            new_node = split_value(num.val)
            new_node.parent = found_parent
            # replace correct child
            if found_parent.l == num:
                found_parent.l = new_node
            elif found_parent.r == num:
                found_parent.r = new_node
            else:
                assert False, "child does not match left or right"

            return True
    return False


def reduce(root):
    while True:
        # you must repeatedly do the first action in this list that applies
        if (explode(root)):
            continue
        if (split(root)):
            continue
        break


def solve1(lines):
    snailfish_numbers = [parse(line.strip()) for line in lines] 

    acc = snailfish_numbers[0]
    for sn in snailfish_numbers[1:]:
        acc = add(acc, sn)
        reduce(acc)
    # print(acc)
    return magnitude(acc)


def solve2(lines):
    perm = list(permutations(range(len(lines)), 2))

    M = []
    for i, j in perm:
        # always parse fresh
        a = parse(lines[i].strip())
        b = parse(lines[j].strip())
        acc = add(a, b)
        reduce(acc)
        m = magnitude(acc)
        M.append(m)

    return max(M)


print(solve1(lines))  # 3574
print(solve2(lines))  # 4763

stop = datetime.now()
print("duration:", stop - start)

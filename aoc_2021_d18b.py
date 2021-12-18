from datetime import datetime

# pypy3.exe .\save.py 18

start = datetime.now()
lines = open('18.in').readlines()
# lines = open('18.ex1').readlines()
# lines = open('18.ex2').readlines()
# lines = open('18.ex3').readlines()
# lines = open('18.ex4').readlines()
# lines = open('18.ex5').readlines()
# lines = open('18.ex6').readlines()


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        if isinstance(self.val, int):
            return str(self.val)
        return f"[{str(self.left)},{str(self.right)}]"


def add(a, b):
    node = Node()
    node.left = a
    node.right = b
    a.parent = node
    b.parent = node
    return node


def split_value(val):
    assert isinstance(val, int)
    node = Node()
    node.left = Node(val // 2)
    node.left.parent = node
    node.right = Node(val - val // 2)
    node.right.parent = node
    return node


def magnitude(node):
    assert isinstance(node, Node)
    if node.val is not None:
        return node.val
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def parse(item):
    node = Node()

    if isinstance(item, int):
        node.val = item
        return node

    if isinstance(item, list):
        node.left = parse(item[0])
        node.right = parse(item[1])
        node.left.parent = node
        node.right.parent = node
        return node

    assert False, "unknown type"


def traverse(node, level):
    assert isinstance(node, Node)

    if node.val is not None:
        print(".."*level, node.val)
        return
    traverse(node.left, level+1)
    traverse(node.right, level+1)


def find_values(node, level, data):
    assert isinstance(node, Node)

    if node.val is not None:
        # print(".."*level, node.val)
        data.append((level, node))
        return
    find_values(node.left, level+1, data)
    find_values(node.right, level+1, data)


def explode(node):
    # collect all values
    values = []
    find_values(node, 0, values)

    for i, v in enumerate(values):
        # print(i,v)
        level, num = v
        if level == 5:
            # found first with level 5

            found_parent = num.parent
            left = found_parent.left.val
            right = found_parent.right.val
            # print(found_parent, left, right)

            # determine which side it is
            # replace node with val 0
            parent_parent = found_parent.parent
            new_node = Node(0)
            new_node.parent = parent_parent
            # replace correct child
            if parent_parent.left == found_parent:
                parent_parent.left = new_node
            elif parent_parent.right == found_parent:
                parent_parent.right = new_node
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


def split(node):
    # collect all values
    values = []
    find_values(node, 0, values)

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
            if found_parent.left == num:
                found_parent.left = new_node
            elif found_parent.right == num:
                found_parent.right = new_node
            else:
                assert False, "child does not match left or right"

            return True
    return False


def reduce(node):
    while True:
        # you must repeatedly do the first action in this list that applies
        if (explode(node)):
            continue
        if (split(node)):
            continue
        break


def solve1(lines):
    snailfish_numbers = [parse(eval(line.strip())) for line in lines]

    acc = snailfish_numbers[0]
    for sn in snailfish_numbers[1:]:
        acc = add(acc, sn)
        reduce(acc)
    # print(acc)
    return magnitude(acc)


def solve2(lines):
    l = len(lines)
    M = []
    for i in range(l):
        for j in range(l):
            if i != j:
                # always parse fresh
                a = parse(eval(lines[i].strip()))
                b = parse(eval(lines[j].strip()))
                acc = add(a, b)
                reduce(acc)
                m = magnitude(acc)
                M.append(m)

    return max(M)


print(solve1(lines))  # 3574
print(solve2(lines))  # 4763

stop = datetime.now()
print("duration:", stop - start)

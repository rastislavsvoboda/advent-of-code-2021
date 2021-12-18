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


def split_(x):
    if x % 2 == 0:
        return SN(Val(x//2), Val(x//2))

    return SN(Val(x//2), Val(x//2+1))


def magnitude(x):
    if type(x) == Val:
        return x.val
    if type(x) == SN:
        return 3 * magnitude(x.l) + 2 * magnitude(x.r)


def level(x):
    if type(x) == Val:
        return 0

    if type(x) == SN:
        return 1 + max(level(x.l), level(x.r))


def parse(str):
    if len(str) == 0:
        return None

    current = ""

    stack=[]
    for x in str:
        if x == '[':
            current = ""
        elif x == ']':
            if current != "":
                stack.append(Val(int(current)))
            r = stack.pop()
            l = stack.pop()
            stack.append(SN(l,r))
            current = ""
        elif x == ',':
            if current != "":
                stack.append(Val(int(current)))
                current = ""
        else:
            current = "" + x

    res =  stack.pop()
    assert len(stack) == 0
    assert res.l is not None
    assert res.r is not None
    return res



def trav(n, ind):

    if type(n) == Val:
        print(".."*ind, n)
        return

    if type(n) == SN:
        l = trav(n.l, ind+1)
        r = trav(n.r, ind+1)

    # print(" "*ind, "xxx", )
    # trav(n.l, ind+1)
    # trav(n.l, ind+1)


def find_vals(n, lev, data):
    if type(n) == Val:
        # print(".."*lev, n)
        data.append((lev, n))
        return

    if type(n) == SN:
        l = find_vals(n.l, lev+1, data)
        r = find_vals(n.r, lev+1, data)




# def solve1_t(text):
#     res = 0

#     data = get_data(text)
#     for d in data:
#         print(d)
#         res += 1

#     return res

# n1 = Snum(1, 2)
# print(n1)
# n2 = Snum(Snum(3, 4), 5)
# print(n2)
# r = add(n1, n2)
# print(r)

# print(split(10))
# print(split(11))
# print(split(12))


# print(level(1))
# print(level(n1))
# print(level(n2))

# d = "[1,2]"
# d = "[[1,2],3]"

# x = parse(d)



# a = "[[[[4,3],4],4],[7,[[8,4],9]]]"
# b = "[1,1]"

# pa = parse(a)
# pb = parse(b)

# # print(level(pa))
# # print(level(pb))

# pc = add(pa, pb)
# print(level(pc))

# print(pc)



def explode(root):
    values = []
    find_vals(root, 0, values)

    found = False
    for i,v in enumerate(values):
        # print(i,v)
        level, num = v
        if level == 5:
            found = True

            found_parent = num.parent
            left = found_parent.l.val
            right = found_parent.r.val
            # print(found_parent, left, right)

            p_p = found_parent.parent
            if p_p.l == found_parent:
                # print("it is left")
                new_node = Val(0)
                p_p.l = new_node
                new_node.parent = p_p

            elif p_p.r == found_parent:
                # print("it is right")

                new_node = Val(0)
                p_p.r = new_node
                new_node.parent = p_p

            else:
                assert False, "not found"

            if i>=1:
                before =   values[i-1][1]
                # print("before:", before)
                before.val += left

            if i<len(values)-2:
                after = values[i+2][1]
                # print("after:", after)
                after.val += right

            break
    return found        

def try_explode(root):
    # trav(root,0)
    # print()
    return explode(root)


def split(root):
    values = []
    find_vals(root, 0, values)

    found = False
    for i,v in enumerate(values):
        # print(i,v)
        level, num = v

        if num.val >= 10:
            found = True

            found_parent = num.parent
            # print(found_parent)

            # p_p = found_parent.parent
            if found_parent.l == num:
                # print("it is left")
                new_node = split_(num.val)
                found_parent.l = new_node
                new_node.parent = found_parent

            elif found_parent.r == num:
                # print("it is right")

                new_node = split_(num.val)
                found_parent.r = new_node
                new_node.parent = found_parent

            else:
                assert False, "not found"

            break
    return found        


def try_split(root):
    # trav(root,0)
    # print()
    return split(root)


# print()

# trav(pc,0)
# print()


def reduce(root):
    canExplode = False
    canSplit = False
    while True:
        canExplode = try_explode(root)
        if canExplode:
            continue

        canSplit = try_split(root)
        if canSplit:
            continue

        break


# print(values)


# reduce(pc)
# print("reduced")
# trav(pc,0)







# p1 = SN(1,2)

# print(p1)

# p1.l = 3
# print(p1)

# print(x)
# print(level(x))
# print(level(x.left))
# print(level(x.right))


# x = add(parse("[1,2]"),parse("[[3,4],5]"))
# print(x)

# ex1 = "[[[[[9,8],1],2],3],4]"
# x= parse(ex1)
# print(x)
# print(level(x))


def test_magnitude():
    m_test = """
[[1,2],[[3,4],5]]
[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
[[[[1,1],[2,2]],[3,3]],[4,4]]
[[[[3,0],[5,3]],[4,4]],[5,5]]
[[[[5,0],[7,4]],[5,5]],[6,6]]
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
""" 


    for x in m_test.split('\n'):
        x = x.strip()
        if x:
            # print(x, len(x))
            v = parse(x)
            print(v)
            print(magnitude(v))

# print(magnitude(parse("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")))



def solve1(lines):
    res = 0

    nums = []
    for line in lines:
        line = line.strip()
        sn = parse(line)
        nums.append(sn)


    # L = []
    # for n in nums:
    #     print(n)
    #     # L.append(level(n))


    acc = nums[0]
    for n in nums[1:]:

        # print(acc)
        # print(n)
        acc = add(acc, n)
        # print(acc)
        reduce(acc)
        # print(acc)
        # print("------")

    print("====")

    print(acc)
    # print("max level:", max(L))
    # print(L)
    print("mag:")


    res = magnitude(acc)

    return res




def solve2(lines):
    perm = list(permutations(range(len(lines)),2))

    M = []
    for i,j in perm:
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

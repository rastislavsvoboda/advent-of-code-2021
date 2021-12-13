from datetime import datetime

# pypy3.exe .\save.py 7

start = datetime.now()
lines = open('7.in').readlines()
# lines = open('7.ex1').readlines()


def cost1(h1, h2):
    dist = abs(h1-h2)
    return dist


def cost2(h1, h2):
    dist = abs(h1-h2)
    # computes ~9sec
    # return sum([i for i in range(0, dist+1)])
    # this can be optimized to: sum of numbers from 0 .. n = n(n+1)/2
    # computes 0.1sec
    return (dist * (dist + 1)) // 2


def solve(nums, minN, maxN, cost_fun):
    F = {}
    for h in range(minN, maxN+1):
        F[h] = sum(cost_fun(x, h) for x in nums)
    return min(F.values())


nums = [int(x) for x in lines[0].strip().split(',')]
N = [int(n) for n in nums]
minN = min(N)
maxN = max(N)

print(solve(N, minN, maxN, cost1))  # 349769
print(solve(N, minN, maxN, cost2))  # 99540554

stop = datetime.now()
print("duration:", stop - start)

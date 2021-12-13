from datetime import datetime

# pypy3.exe .\save.py 7

start = datetime.now()
lines = open('7.in').readlines()
# lines = open('7.ex1').readlines()


def cost2(h1, h2):
    dist = abs(h1-h2)
    # computes ~9sec
    # return sum([i for i in range(0, dist+1)])
    # this can be optimized to: sum of numbers from 0 .. n = n(n+1)/2
    # computes 0.1sec
    return (dist * (dist + 1)) // 2


nums = [int(x) for x in lines[0].strip().split(',')]
N = [int(n) for n in nums]
# print(N)
N.sort()
minN = N[0]
maxN = N[-1]
med = N[len(N)//2]
# print(minN, maxN, med)

s1 = sum(abs(n-med) for n in N)
print(s1) # 349769

F = {}
for h in range(minN, maxN+1):
    F[h] = sum(cost2(n, h) for n in nums)
s2 = min(F.values())
print(s2) # 99540554

stop = datetime.now()
print("duration:", stop - start)

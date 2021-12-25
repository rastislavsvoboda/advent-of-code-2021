from datetime import datetime
import re
from collections import defaultdict, Counter, deque
import sys

#submit(len(G), part="a", day=20, year=2021)
start = datetime.now()
infile = sys.argv[1] if len(sys.argv)>1 else '22.in'
# infile = sys.argv[1] if len(sys.argv)>1 else '22.ex3'

data = open(infile).read().strip()

# [1 10] [11 20] [21 100]
X = set()
Y = set()
Z = set()
C = []
min_x = 0
min_y = 0
min_z = 0
max_x = 0
max_y = 0
max_z = 0
G = set()
for r,line in enumerate(data.strip().split('\n')):
  assert line == line.strip()
  words = line.split()
  cmd = words[0]
  x1,x2,y1,y2,z1,z2 = [int(x) for x in re.findall('-?\d+', words[1])]
  x1,x2 = min(x1, x2), max(x1,x2)
  y1,y2 = min(y1, y2), max(y1,y2)
  z1,z2 = min(z1, z2), max(z1,z2)

  X.add(x1)
  X.add(x2+1)
  Y.add(y1)
  Y.add(y2+1)
  Z.add(z1)
  Z.add(z2+1)

  min_x = min(x1, min_x)
  min_y = min(y1, min_y)
  min_z = min(z1, min_z)
  max_x = max(x2, max_x)
  max_y = max(y2, max_y)
  max_z = max(z2, max_z)
  C.append((x1,x2,y1,y2,z1,z2,cmd=='on'))

def expand(A):
  B = sorted(A)
  ret = {}
  for i, v in enumerate(B):
      ret[v] = i
  U = [v2-v1 for v1, v2 in zip(B, B[1:])]
  return (ret, U)


X.add(-50)
X.add(51)
Y.add(-50)
Y.add(51)
Z.add(-50)
Z.add(51)

X,UX = expand(X)
Y,UY = expand(Y)
Z,UZ = expand(Z)

#print(len(X), len(Y), len(Z))

def solve(p1):
  G = set()
  for t,(x1,x2,y1,y2,z1,z2,on) in enumerate(C):
    #print(t,len(C))
    if p1:
      x1 = max(x1, -50)
      y1 = max(y1, -50)
      z1 = max(z1, -50)
      
      x2 = min(x2, 50)
      y2 = min(y2, 50)
      z2 = min(z2, 50)
    for x in range(X[x1], X[x2+1]):
      for y in range(Y[y1], Y[y2+1]):
        for z in range(Z[z1], Z[z2+1]):
          #print(x,y,z,UX[x],UY[y],UZ[z])
          if on:
            G.add((x,y,z))
          else:
            G.discard((x,y,z))

  ans = 0
  for x,y,z in G:
    lx = UX[x]
    ly = UY[y]
    lz = UZ[z]
    ans += lx*ly*lz
  return ans

# print(solve(True))
print(solve(False))

stop = datetime.now()
print("duration:", stop - start)

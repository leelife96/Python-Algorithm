import sys

N = int(sys.stdin.readline())
pyo = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pyo.append([x, y])

pyo.sort(key = lambda x : (x[1], x[0]))

for x, y in pyo:
    print(x, y)

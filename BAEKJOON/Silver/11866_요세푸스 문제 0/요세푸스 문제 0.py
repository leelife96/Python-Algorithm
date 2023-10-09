from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
res = []
# dq = deque()
# for i in range(1, N+1):
#     dq.append(i)
dq = deque([i for i in range(1, N+1)])

while len(dq) != 0:
    for _ in range(K-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())

print('<', end='')
for i in range(len(res) - 1):
    print("%d, "%res[i], end='')
print(res[-1], end='')
print('>', end='')


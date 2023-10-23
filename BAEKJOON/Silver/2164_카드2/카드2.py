import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque(list(i for i in range(1, N+1)))

while len(deq)>1:
    deq.popleft()
    temp = deq.popleft()
    deq.append(temp)

print(deq[0])
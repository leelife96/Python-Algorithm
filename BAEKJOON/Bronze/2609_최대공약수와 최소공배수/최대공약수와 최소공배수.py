import sys

N, K = map(int, sys.stdin.readline().split())
list = []
for i in range(1 ,min(N, K)+1):
    if N % i == 0 and K % i == 0:
        list.append(i)
print(max(list))
print(max(list) * (N//max(list) * K//max(list)))

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)


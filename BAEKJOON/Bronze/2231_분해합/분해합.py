import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == N:
        print(i)
        break
    if i == N:
        print(0)

import sys

N = int(sys.stdin.readline())
bees_start = 1
cnt = 1
while N > bees_start:
    bees_start += 6*cnt
    cnt += 1
print(cnt)
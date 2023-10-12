import sys

N = int(input())
arr = []
for _ in range(N):
    X, Y = sys.stdin.readline().split()
    X = int(X)
    arr.append([X, Y])

arr.sort(key=lambda x : x[0])
for X, Y in arr:
    print(X, Y)

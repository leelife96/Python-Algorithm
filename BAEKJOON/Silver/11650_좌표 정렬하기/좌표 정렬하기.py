import sys

N = int(sys.stdin.readline())
list = []
for i in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    list.append([X, Y])

list.sort(key=lambda x : (x[0],x[1]))

for X, Y in list:
    print(X, Y)
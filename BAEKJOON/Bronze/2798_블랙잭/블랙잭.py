import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_list = []
print(arr)
for i in range(N):
    A = arr.pop()
    sum_list = list(A)
    for j in list(sum_list):
        if sum_list[j]+sum_list[j+1] > sum(sum_list[j]+sum_list[j+1]):
            print()






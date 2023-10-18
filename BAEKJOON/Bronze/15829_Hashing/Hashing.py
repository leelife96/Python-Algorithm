import sys

L = int(sys.stdin.readline())
arr_list = list(sys.stdin.readline())

answer = 0
sum = 0

for i in range(L):
    answer = (ord(arr_list[i])-96) * (31**i)
    sum += answer

print(sum % 1234567891)

import sys

# N=배열의크기, M=숫자가 더해지는 횟수, K=배열의 특정한 인덱스(번호)에 해당하는 수가 연속~
N, M, K = map(int,sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1
print(result)







# min(), max() 함수를 이용하는 답안 예시
import sys

N, M = map(int, sys.stdin.readline().split())

card = []
min_list = []
for i in range(N):
    card.append(list(map(int,sys.stdin.readline().split())))
    min_value = min(card[i])
    min_list.append(min_value)

print(max(min_list))

# 2중 for문을 이용하는 답안 예씨

import sys

N, M = map(int, sys.stdin.readline().split())
result = 0
for i in range(N):
    card = list(map(int,sys.stdin.readline().split()))
    min_value = 10001
    for i in card:
        min_value = min(min_value, i)
    result = max(result, min_value)
print(result)









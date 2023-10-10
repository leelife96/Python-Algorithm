import sys

N = int(sys.stdin.readline())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = list(map(int, sys.stdin.readline().split()))

for coin in coin_types:
    count = count + (N// coin) # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    N %= coin
print(count)

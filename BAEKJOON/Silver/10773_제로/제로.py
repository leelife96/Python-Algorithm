import sys

K = int(sys.stdin.readline())
money_list = []

for i in range(K):
    money = int(sys.stdin.readline())
    if money == 0:
        money_list.pop()
    else:
        money_list.append(money)

kk = sum(money_list)
print(kk)
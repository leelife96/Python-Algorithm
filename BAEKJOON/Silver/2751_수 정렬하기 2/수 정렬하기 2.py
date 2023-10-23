import sys

N = int(sys.stdin.readline())
salt_list = []
for _ in range(N):
    salt_list.append(int(sys.stdin.readline()))


salt_list.sort()
for i in salt_list:
    print(i)
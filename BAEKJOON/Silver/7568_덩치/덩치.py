import sys

N = int(sys.stdin.readline())
chi_list = []
for i in range(N):
    chi_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if (chi_list[i][0] < chi_list[j][0]) and (chi_list[i][1] < chi_list[j][1]):
                rank += 1
    print(rank, end=' ')
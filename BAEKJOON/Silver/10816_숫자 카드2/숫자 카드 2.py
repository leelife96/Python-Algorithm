import sys
from collections import Counter

N = int(sys.stdin.readline())
first_line = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
second_line = list(map(int, sys.stdin.readline().split()))

c = Counter(first_line)

for i in second_line:
    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')

# Counter(["h1", "hey", "hi", "hi", "hello", "hey" ])
# print(Counter(["h1", "hey", "hi", "hi", "hello", "hey" ]))
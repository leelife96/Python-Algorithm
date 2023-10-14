import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    num = sys.stdin.readline().split()

    if num[0] == 'push':
        stack.append(num[1])

    elif num[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif num[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif num[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif num[0] == 'size':
        print(len(stack))





import sys

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    num = sys.stdin.readline().split()

    if num[0] == 'push':
        queue.append(num[1])
    elif num[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif num[0] == 'size':
        print(len(queue))

    elif num[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif num[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif num[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


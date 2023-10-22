import sys

T = int(sys.stdin.readline())

for _ in range(T):
    VPS = sys.stdin.readline()
    stack = []
    for i in VPS:
        if i == '(':
            stack.append('(')

        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        else:
            break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

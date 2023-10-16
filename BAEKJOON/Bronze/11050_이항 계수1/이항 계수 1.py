import sys
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)


N, K = map(int, sys.stdin.readline().split())
print(factorial(N) // (factorial(K) * factorial(N-K)))


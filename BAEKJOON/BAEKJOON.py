"""
a,b=map(float,input().split())
print(a*b)
//6036
"""
import sys

"""
n = input()
s = input()
print(int(n)*s) //6037 """

"""a,b=map(int,input().split())

c = a**b
print(c) //6038 """

""" f1,f2=map(float,input().split())
print(f1**f2)  //6039 """

""" a,b=map(int,input().split())
print(a//b) //6040 """

""" a = input()
a = float(a)
print(format(a,".2f")) //6042 """

""" f1,f2=map(float,input().split())
print(format(f1/f2,".3f")) //6043 """

""" a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f")) //6044 """

""" a,b,c=(int,input().split())
print(a+b+c)
print(format((a+b+c)/3,".2f")) //6045 """


"""array = []

for i in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if (array[x][y] == 0):
        array[x][y] = 9
    elif (array[x][y] == 2):
        array[x][y] = 9
        break

    if ((array[x][y+1] == 1 and array[x+1][y] == 1)):
        break

    if (array[x][y+1] != 1):
        y = y + 1
    elif (array[x+1][y] != 1):
        x = x + 1

for i in range(10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()  // 6098 """

"""a = dict()
a['홍길동'] = 97
a['이순신'] = 98
print(a)

b = {
    '홍길동' : 97, 
    '이순신' : 98
}
print(b)
print(b['이순신'])

key_list = list(b.keys())
print(key_list)"""

"""data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
"""

# import sys
#
# data = sys.stdin.readline().rstrip()
# print(data)

#
# a = int(input())
#
# for i in range(1, 10):
#     print(a, '*', i, '=', a*i)

# a = int(input())
#
# for i in range(1, a+1):
#     print("*" * i)



# while True:
#     try:
#         a, b = map(int,input().split())
#         print(a+b)
#     except:
#         break

# import sys
#
# A = []
# B = []
#
# N, M = map(int, sys.stdin.readline().split())
#
# for i in range(N):
#     i = list(map(int, sys.stdin.readline().split()))
#     A.append(i)
#
# for i in range(N):
#     i = list(map(int, sys.stdin.readline().split()))
#     B.append(i)
#
# for i in range(N):
#     for j in range(M):
#         print(A[i][j] + B[i][j], end=' ')
#     print()

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
#
#
# import sys
#
# A = sys.stdin.readlines()
#
# for i in A:
#     print(i.rstrip())


# import sys
#
# # T = int(input())
# #
# # for i in range(0, T):
# #     A = input()
# #     print(A[0] + A[-1])
#
#
# import sys
#
# # A = sys.stdin.readlines()
#
# import sys
#
# T = int(sys.stdin.readline())
#
# for i in range(0, T):
#     A = sys.stdin.readline().rstrip()
#     print(A[0] + A[-1])

# import sys
#
# A, B = map(int, sys.stdin.readline().split())
#
# print((A+B)*(A-B))

# import sys
#
# a, b, c, d, e = map(int, sys.stdin.readline().split())
#
# sum = (a ** 2)+(b ** 2)+(c ** 2)+(d ** 2)+(e ** 2)
#
# print(sum % 10)

# import sys
#
# T = int(sys.stdin.readline())
#
# for i in range(T):
#     H, W, N = map(int, sys.stdin.readline().split())
#
#     floor = N % H
#     room_num = (N // H) + 1
#     if N % H == 0:
#         floor = H
#         room_num = N // H
#     print(100*floor + room_num)

# import sys
# S = sys.stdin.readline().strip()
# alpha = [chr(i) for i in range(97, 123)]
# for x in alpha:
#    print(S.find(x), end=' ')

# import sys
#
# while True:
#     A, B, C = map(int, sys.stdin.readline().split())
#
#     if A==0 and B==0 and C==0 :
#         break
#     A = pow(A, 2)
#     B = pow(B, 2)
#     C = pow(C, 2)
#
#     if A+B == C or A+C == B or B+C == A:
#         print("right")
#     else:
#         print("wrong")
# import sys
# #계수정렬 활용
# N = int(sys.stdin.readline())
# arr = [0] * (10000+1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언
# #각 입력값에 해당하는 인덱스의 값 증가
# for _ in range(N):
#     arr[int(sys.stdin.readline())] += 1
# #arr에 기록된 정보 확인
# for i in range(len(arr)):
#     if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
#         for _ in range(arr[i]):
#             print(i)

# import sys
# N = int(sys.stdin.readline())
# prime = list(map(int, sys.stdin.readline().split()))
# count = 0
#
# for i in prime:
#     error = 0
#     if i > 1:
#          for j in range(2, i):
#              if i % j == 0:
#                  error += 1
#          if error == 0:
#              count += 1
# print(count)

# import sys
#
# N = int(sys.stdin.readline())
# word = []
# for _ in range(N):
#     word.append(sys.stdin.readline().strip())
#
# word = list(set(word)) ## word의 중복된 요소를 제거하고 리스트로 다시 만듬
# word.sort() ## 사전 순서대로 정렬함
# word.sort(key=len) ## key=len을 주어서 짧은 길이 순으로 다시 정렬
#
# for i in word:
#     print(i)

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
res = []
dq = deque([i for i in range(1, N+1)])
while len(dq) != 0:
    for i in range(K-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())

print('<', end='')
for i in range(len(res)-1):
    print("%d, " % res[i], end='')
print(res[-1], end='')
print('>', end='')


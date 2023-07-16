"""
a,b=map(float,input().split())
print(a*b)
//6036
"""


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


array = []

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
    print()


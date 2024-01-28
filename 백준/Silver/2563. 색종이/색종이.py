from sys import stdin as s
a = [[ 0 for i in range(100)]for i in range(100)]
N = int(input())
for i in range(N):
    x, y = map(int, s.readline().split())
    for i in range(x-1,x+9):
        for j in range(y-1, y +9):
            a[j][i] = 1
result = 0
for i in range(100):
    for j in range(100):
        if a[i][j] == 1:
            result +=1

print(result)
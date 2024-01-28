from sys import stdin as s
N, M = map(int,s.readline().split())
a = []
for i in range(N):
    a.append(list(map(int, s.readline().split())))
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        a[i][j] = a[i][j]+temp[j]
for k in range(N):
    print(*a[k])
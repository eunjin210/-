N, M = map(int,input().split())
a = []
for i in range(N):
    temp = list(map(int, input().split()))
    a.append(temp)
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        a[i][j] = a[i][j]+temp[j]
for k in range(N):
    print(*a[k])
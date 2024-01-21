N, M = map(int, input().split())
arr =[]
a = N*[0]
for i in range(N):
    arr.append(i+1)
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j]= arr[i-1:j][::-1]

for i in range(N):
    print(arr[i], end =' ')
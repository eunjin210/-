N, M = map(int, input().split())
arr =[]
for i in range(N):
    arr.append(i+1)

for _ in range(M):
    i, j = map(int, input().split())
    for right in range((j-i)//2+1):
        left = j-1-right
        temp = arr[left]
        arr[left] = arr[right+i-1]
        arr[right+i-1] = temp

for i in range(N):
    print(arr[i], end =' ')
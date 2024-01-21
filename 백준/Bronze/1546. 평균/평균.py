N = int(input())
sum = 0
num = list(map(int,input().split()))
M = max(num)
for i in range(N):
    sum += num[i]/M*100
print(sum/N)

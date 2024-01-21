N = int(input())
L = list(map(int, input().split()))
F = int(input())
result = 0
for i in L:
    if i == F:
        result +=1
print(result)
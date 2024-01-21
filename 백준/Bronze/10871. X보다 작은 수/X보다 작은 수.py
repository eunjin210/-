N, F = map(int, input().split())
L = list(map(int, input().split()))
for i in range(N):
    if L[i] < F:
        print(L[i], end =' ')
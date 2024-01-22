n = int(input())
for _ in range(n):
    count, s = input().split()
    for i in range(len(s)):
        print(s[i]*int(count),end='')
    print()
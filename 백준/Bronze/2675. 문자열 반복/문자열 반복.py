n = int(input())
for _ in range(n):
    count, s = input().split()
    print(''.join(ch*int(count) for ch in s))
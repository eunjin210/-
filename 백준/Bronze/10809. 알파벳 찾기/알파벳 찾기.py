s = input()
arr = [-1]*26
for i in range(len(s)):
    num = ord(s[i])-97
    if arr[num] == -1:
        arr[num] = i
print(*arr)
s = input()
length = len(s)//2
result = 1
for i in range(length):
    if s[i] == s[-1*(i+1)]:
        continue
    else:
        result =0
        break
print(result)
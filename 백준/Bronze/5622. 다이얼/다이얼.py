result = 0
s = input()

for i in range(len(s)):
    if 65<=ord(s[i])<=67:
        result += 3
    if 68<=ord(s[i])<=70:
        result += 4
    if 71<=ord(s[i])<=73:
        result += 5
    if 74<=ord(s[i])<=76:
        result += 6
    if 77<=ord(s[i])<=79:
        result += 7
    if 80<=ord(s[i])<=83:
        result += 8
    if 84<=ord(s[i])<=86:
        result += 9
    if 87<=ord(s[i])<=90:
        result += 10
print(result)
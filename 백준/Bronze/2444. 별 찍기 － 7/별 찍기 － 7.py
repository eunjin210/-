s = int(input())
for i in range(s):
    print(' '*(s-i-1)+'*'*(1+2*i))
for i in range(s-1):
    print(' '*(i+1)+'*'*((s-i-2)*2+1))
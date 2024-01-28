N = int(input())
temp = 1
level = 1
while N != level:
    N = N - temp
    if N <= level:
        level +=1
        break
    temp +=1
    level +=1
if level % 2 ==0:
    print(N,end='')
    print('/',end='')
    print(level - N +1)
else:
    print(level - N +1,end='')
    print('/',end='')
    print(N,end='')

N = int(input())
length = 0
temp = N
result = 0

if N == 0:
    length +=1

while result != N:
    if 0< temp <10:
        result = temp+10*temp
        length +=1
    else:
        result = temp//10 + temp%10
        result = (temp%10)*10 + (result%10)
        length += 1
    temp = result

print(length)
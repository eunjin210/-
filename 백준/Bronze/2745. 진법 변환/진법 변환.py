num, system = input().split()
num = num[::-1]
numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i,n in enumerate(num):
    result += (int(system)**i)*(numbers.index(n))
print(result)
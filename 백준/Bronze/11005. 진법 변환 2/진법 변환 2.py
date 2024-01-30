num, system = map(int,input().split())
numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = []
while(num // system !=0):
    arr.append(str(numbers[num % system]))
    num = num // system

arr.append(str(numbers[num % system]))
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end='')
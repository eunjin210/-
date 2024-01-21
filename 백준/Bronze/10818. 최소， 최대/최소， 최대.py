N = int(input())
list1 = list(map(int, input().split()))

i = 0
MAX = list1[0]
MIN = list1[0]
for i in range(N):
    if int(list1[i]) < MIN:
        MIN = int(list1[i])

    if int(list1[i]) > MAX:
        MAX = int(list1[i])

print(MIN,MAX)
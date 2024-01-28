from sys import stdin as s
a = [] # 값을 입력하면, 9X10행렬이 만들어짐
row = 0
cal = 0
max = 0
for i in range(9):
    a.append(list(map(int, s.readline().split())))
    for j in range(9):
        if max <= a[i][j]:
            max = a[i][j]
            cal = i+1
            row = j+1
print(max)
print(cal, row)
arr = []
for _ in range(10):
    n = int(input())
    result = n % 42
    if result not in arr:
        arr.append(result)
print(len(arr))
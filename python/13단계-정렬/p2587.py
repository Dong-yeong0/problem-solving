arr = []
for _ in range(5):
    arr.append(int(input()))
    
arr.sort()
print(int(sum(arr) / 5))
print(arr[len(arr) // 2])
N = int(input())

arr = []
for _ in range(N):
    decimal = int(input())
    arr.append(decimal)
    
arr.sort()
for i in arr:
    print(i)
    
# 미친문제
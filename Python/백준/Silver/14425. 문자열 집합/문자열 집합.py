n, m = map(int, input().split())
s = {}
for _ in range(n):
    s[input().strip()] = 0

answer = 0
for _ in range(m):
    word = input()
    if word in s:
        answer += 1
    
print(answer)
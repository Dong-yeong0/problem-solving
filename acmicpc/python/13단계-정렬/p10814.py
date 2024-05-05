import sys

"""
! python 내장 함수 input() 사용
* Memory: 48324KB
* Time: 4324ms
"""
# N = int(input())

# arr = []
# for _ in range(N):
#     age, name = map(str, input().split())
#     arr.append([int(age), name])
    
# arr.sort(key=lambda x:x[0])

# for i in arr:
#     print(*i, sep=' ')

"""
! sys.stdin.readline() 사용
* Memory: 48324KB
* Time: 312ms
"""

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    arr.append([int(age), name])

arr.sort(key=lambda x:x[0])

for i in arr:
    print(*i, sep=' ')
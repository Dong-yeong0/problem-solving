"""
! 10813 공 바꾸기
* Memory: 31256 KB
* Time: 44 ms
"""
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [str(i + 1) for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]
    
print(' '.join(arr)) 
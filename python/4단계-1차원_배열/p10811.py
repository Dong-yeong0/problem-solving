"""
! 10811 바구니 뒤집기
* Memory: 31256 KB
* Time: 40 ms
"""

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1:j] = reversed(arr[i-1:j])
    
print(*arr)
    
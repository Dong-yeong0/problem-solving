"""
! 2501 약수 구하기
* Memory: 31256 KB
* Time: 40 ms
"""

import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
count = 0

for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)
    count += 1

if K > len(arr):
    print(0)
else:
    print(arr[K-1])
"""
! 2738 행렬 덧셈
* Memory: 31256 KB
* Time: 52 ms

in
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

out
4 4 4
6 6 6
5 6 100
"""
import sys

N, M = map(int, sys.stdin.readline().split())
A, B = [], []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
    
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))
    
# print(A)
# [[1, 1, 1], [2, 2, 2], [0, 1, 0]]

# print(B)
# [[3, 3, 3], [4, 4, 4], [5, 5, 100]]

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()
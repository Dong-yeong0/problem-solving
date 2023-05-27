"""
! 2720 세탁소 사장 동혁
* Memory: 31256 KB
* Time: 44 ms
"""

import sys

T = int(sys.stdin.readline())
changes = [25, 10, 5, 1]

for _ in range(T):
    C = int(sys.stdin.readline())
    response = []
    for i in changes:
        response.append(C // i)
        C %= i
    print(*response)
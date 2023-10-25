"""
! 2903 중앙 이동 알고리즘
* Memory: 31120 KB
* Time: 40ms

In
1
---
2
---
5

Out
9
---
25
---
1089
---
"""
import sys
N = int(sys.stdin.readline())
print((1 + 2 ** N) ** 2)
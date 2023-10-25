"""
! 1085 직사각형에서 탈출
* Memory: 31120 KB
* Time: 40 ms

In
6 2 10 3
---
1 1 5 5
---
653 375 1000 1000
---
161 181 762 375

Out
1
---
1
---
347
---
161
"""
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, w - x, h - y))
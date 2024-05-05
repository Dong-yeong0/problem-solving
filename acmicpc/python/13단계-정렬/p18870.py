"""
! 18870 좌표압축
! 시간제한: 2초
! 메모리 제한: 512MB
* Memory: 
* Time:

In
5
2 4 -10 4 -9
---
6
1000 999 1000 999 1000 999

Out
2 3 0 3 1
---
1 0 1 0 1 0
"""

import math
import sys
R = int(sys.stdin.readline())

print(f"반지름 {R}의 면적은 {3.14 * R * 2}")
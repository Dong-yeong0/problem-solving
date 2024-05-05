"""
! 2563 색종이
* Memory: 
* Time:

In
3
3 7
15 7
5 2

Out
260
"""

import sys

white_paper = [[0 for _ in range(100)] for _ in range(100)]

color_paper = int(sys.stdin.readline())

for _ in range(color_paper):
    x, y = list(map(int, sys.stdin.readline().split()))
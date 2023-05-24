"""
! 1934 최소공배수
* Memory: 
* Time:

? ref: https://baby-dev.tistory.com/97
유클리드 호제법 사용
"""

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    
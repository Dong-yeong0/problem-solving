"""
! 10798 세로읽기
* Memory: 31256 KB
* Time: 44 ms

! 각 줄에는 최소 1개, 최대 15개의 글자, 빈칸 없이
! 총 5줄
! A~Z, a~z, 0~9
! 각 줄의 시작과 마지막에 빈칸 X

In
ABCDE
abcde
01234
FGHIJ
fghij

Out
Aa0FfBb1GgCc2HhDd3IiEe4Jj
"""

import sys

words = [sys.stdin.readline().rstrip() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')
    
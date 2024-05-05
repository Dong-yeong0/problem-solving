"""
! 1181 단어 정렬 
* Memory: 35868 KB
* Time: 76 ms
"""

import sys

N = int(sys.stdin.readline())

word = []
for _ in range(N):
    # str.strip() => 선, 후행 문자, 공백 제거
    word.append(sys.stdin.readline().strip())
    
word = list(set(word))
word.sort()
word.sort(key=len)
for i in word:
    print(i)
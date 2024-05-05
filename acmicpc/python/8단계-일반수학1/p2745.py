"""
! 2745 진법 변환
* Memory: 31388 KB
* Time: 40 ms
enumerate() => index, element로 이루어진 tuple로 만들어 줌.

"""
import sys

B, N = map(str ,sys.stdin.readline().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

B = B[::-1]
response = 0

for i, n in enumerate(B):
    response += (int(N) ** i) * (ary.index(n))
print(response)
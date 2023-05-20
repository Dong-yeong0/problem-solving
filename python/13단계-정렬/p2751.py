"""
! 2751 수 정렬하기 2
! N(1 ≤ N ≤ 1,000,000)
* Memory: 84924 KB
* Time: 1388 ms
미친문제 
list.sort() => 리스트 자료형 메소드이며 원본값을 직접 수정한다.
sorted() => python 내장함수로, 리스트 원본은 그대로이며, 정렬 된 복사본을 return 한다.
나중에 list.sort(), sorted() 비교 (데이터는 100만개 정도)
"""
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    decimal = int(sys.stdin.readline())
    arr.append(decimal)
    
for i in sorted(arr):
    print(i)

# 시간초과
# N = int(input())

# arr = []
# for _ in range(N):
#     decimal = int(input())
#     arr.append(decimal)
    
# arr.sort()
# for i in arr:
#     print(i)
    
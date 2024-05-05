import sys

# N => 10,000보다 작거나 같은 자연수
N = int(sys.stdin.readline())
num_arr = [0] * 10001

for _ in range(N):
    num_arr[int(sys.stdin.readline())] += 1

for i in range(len(num_arr)):
    if num_arr[i] != 0:
        for j in range(num_arr[i]):
            print(i)

# 메모리 초과
# N = int(sys.stdin.readline())

# arr = []
# for _ in range(N):
#     # ! for문 속에서 append를 사용하면, 메모리 재할당이 이루어진다. 즉 메모리를 효율적으로 사용 못함
#     arr.append(int(sys.stdin.readline()))
    
# arr.sort()

# for i in arr:
#     print(i, sep='\n')
    

    

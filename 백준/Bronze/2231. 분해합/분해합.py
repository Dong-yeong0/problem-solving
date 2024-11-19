def get_decomposition_sum(num: int) -> int:
    total = num
    while num > 0:
        total += num % 10
        num //= 10

    return total


N = int(input())
for i in range(1, N + 1):
    if get_decomposition_sum(i) == N:
        print(i)
        break
else:
    print(0)

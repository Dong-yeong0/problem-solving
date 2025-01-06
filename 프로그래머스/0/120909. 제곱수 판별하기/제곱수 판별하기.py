def solution(n):
    n_sqrt = n ** 0.5
    sqrt_split = str(n_sqrt).split(".")
    decimal = int(sqrt_split[1])
    return 1 if decimal == 0 else 2
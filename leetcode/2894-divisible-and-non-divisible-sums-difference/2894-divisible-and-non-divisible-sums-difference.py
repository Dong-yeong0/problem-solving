class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        k = n // m
        sum_divisible_by_m = m * (k * (k + 1)) // 2
        num1 = total_sum - sum_divisible_by_m
        num2 = sum_divisible_by_m
        return num1 - num2
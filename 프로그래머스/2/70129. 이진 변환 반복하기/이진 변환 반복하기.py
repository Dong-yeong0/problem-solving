def solution(s):
    count_transformations = 0
    total_removed_zeros = 0
    while s != "1":
        removed_zeros = s.count('0')
        total_removed_zeros += removed_zeros
        s = s.replace('0', '')
        length_after_removal = len(s)
        s = bin(length_after_removal)[2:]
        count_transformations += 1

    return [count_transformations, total_removed_zeros]
def solution(my_string: str, is_prefix: str):
    return 1 if my_string[:len(is_prefix)] == is_prefix else 0

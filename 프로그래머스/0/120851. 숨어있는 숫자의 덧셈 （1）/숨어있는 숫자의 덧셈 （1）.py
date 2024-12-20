def solution(my_string):
    return sum([int(word) for word in my_string if word.isnumeric()])
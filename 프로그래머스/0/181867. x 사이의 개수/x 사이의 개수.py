def solution(myString):
    split_strings = myString.split('x')
    lengths = [len(char_x) for char_x in split_strings]
    return lengths
def solution(my_string, s, e):
    target = my_string[s:e+1][::-1]
    return my_string[:s] + target + my_string[e+1:]
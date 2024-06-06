def solution(myString, pat):
    swapped_str = ''
    for char in myString:
        if char == 'A':
            swapped_str += 'B'
        elif char == 'B':
            swapped_str += 'A'
    
    if pat in swapped_str:
        return 1
    else:
    	return 0

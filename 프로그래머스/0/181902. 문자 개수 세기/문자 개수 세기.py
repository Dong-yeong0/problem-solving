def solution(my_string):
    """
    char_map = {}
    for i in  range(ord('Z') - ord('A') + 1):
        char_map[chr(ord('A') + i)] = 0
        char_map[chr(ord('a') + i)] = 0
        
    char_map = {k: y for k, y in sorted(char_map.items(), key=lambda item: item[0])}
    for char in my_string:
        if char in char_map:
            char_map[char] += 1
    
    return list(char_map.values())
    """
    answer = [0] * 52
    for word in my_string:
        if ord("A") <= ord(word) <= ord("Z"):
            answer[ord(word) - ord("A")] += 1
        else:
            answer[ord(word) - ord("a") + 26] += 1
    
    return answer    

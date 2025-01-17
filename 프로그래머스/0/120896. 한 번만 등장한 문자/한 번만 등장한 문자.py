def solution(s):
    s_words = {}
    for char in s:
        if char not in s_words:
            s_words[char] = 1
        else:
            s_words[char] += 1
    
    answer = ""
    for char, count in s_words.items():
        if count == 1:
            answer += char
            
    return "".join(sorted(answer))
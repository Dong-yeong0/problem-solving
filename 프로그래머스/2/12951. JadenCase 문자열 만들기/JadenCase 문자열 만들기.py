def solution(s):
    words = s.split(' ')
    jaden_case_words = []
    for word in words:
        if word:
            jaden_case_word = word[0].upper() + word[1:].lower()
            jaden_case_words.append(jaden_case_word)
        else:
            jaden_case_words.append('')
            
    return ' '.join(jaden_case_words)
def solution(spell, dic):
    sorted_spell = ''.join(sorted(spell))
    for word in dic:
        if sorted_spell == ''.join(sorted(word)):
            return 1
    
    return 2
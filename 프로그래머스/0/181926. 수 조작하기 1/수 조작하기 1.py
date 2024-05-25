def solution(n, control):
    action_map = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for action in control:
        n += action_map[action]
            
    return n
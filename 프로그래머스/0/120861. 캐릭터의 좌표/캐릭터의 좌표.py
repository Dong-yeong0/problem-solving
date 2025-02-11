def solution(keyinput, board):
    x, y = 0, 0
    max_x = (board[0] // 2)
    max_y = (board[1] // 2)
    move_dict = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    for key in keyinput:
        if key in move_dict:
            dx, dy = move_dict[key]
            new_x = x + dx
            new_y = y + dy
            if -max_x <= new_x <= max_x:
                x = new_x
            if -max_y <= new_y <= max_y:
                y = new_y
    
    return [x, y]
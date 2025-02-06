def solution(numbers):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    answer = ""
    current_word = ""
    for char in numbers:
        current_word += char
        if current_word in num_dict:
            answer += num_dict[current_word]
            current_word = ""
    
    return int(answer)
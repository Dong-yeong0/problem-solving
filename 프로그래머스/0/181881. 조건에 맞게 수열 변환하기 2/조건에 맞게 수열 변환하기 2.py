def transform(arr):
        new_arr = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 == 1:
                new_arr.append(num * 2 + 1)
            else:
                new_arr.append(num)
        return new_arr

def solution(arr):
    answer = 0
    current_arr = arr
    while True:
        next_arr = transform(current_arr)
        if current_arr == next_arr:
            return answer
        current_arr = next_arr
        answer += 1

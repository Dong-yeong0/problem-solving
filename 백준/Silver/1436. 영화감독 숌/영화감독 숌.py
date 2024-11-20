def is_end_number(num):
    return "666" in str(num)

N = int(input())
count = 0
current_number = 666

while True:
    if is_end_number(current_number):
        count += 1
        if count == N:
            print(current_number)
            break
    
    current_number += 1

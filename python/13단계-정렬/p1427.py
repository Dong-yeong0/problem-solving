number = list(map(int, input()))
number.sort(reverse=True)
for i in number:
    print(i, end='')
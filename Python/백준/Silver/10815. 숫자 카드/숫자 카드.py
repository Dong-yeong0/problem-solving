n = input()
cards = list(map(int, input().split()))
m = input()
checks = list(map(int, input().split()))
_dict = {}
for card in cards:
    _dict[card] = 0
    
for check in checks:
    if check in _dict:
        print(1, end=" ")
    else:
        print(0, end=" ")
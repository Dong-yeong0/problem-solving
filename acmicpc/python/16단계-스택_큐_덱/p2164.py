from collections import deque

def last_remaining_card(N):
    cards = deque(range(1, N + 1))
    
    while len(cards) > 1:
        cards.popleft()
        cards.rotate(-1)
        
    return cards[0]

N = int(input())
print(last_remaining_card(N))

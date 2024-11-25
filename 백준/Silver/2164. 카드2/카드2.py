from collections import deque

cards = deque(list(range(1, int(input()) + 1)))

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)
    
print(cards[0])
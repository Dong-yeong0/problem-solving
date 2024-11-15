PAPER_SIZE = 100
PAPER_CUT_SIZE = 10
canvas = [[0] * PAPER_SIZE for _ in range(PAPER_SIZE)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(PAPER_CUT_SIZE):
        for j in range(PAPER_CUT_SIZE):
            canvas[y + j][x + i] = 1
            
black_area = sum(sum(row) for row in canvas)
print(black_area)
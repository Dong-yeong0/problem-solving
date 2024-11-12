points = [tuple(map(int, input().split())) for _ in range(3)]
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]
x, y = 0, 0
for i in range(3):
    if x_coords.count(x_coords[i]) == 1:
        x = x_coords[i]

    if y_coords.count(y_coords[i]) == 1:
        y = y_coords[i]

print(x, y)
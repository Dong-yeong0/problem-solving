x = int(input())
total_price = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    total_price += a * b

print("Yes") if total_price == x else print("No")
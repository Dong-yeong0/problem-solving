def solution(price, money, count):
    total_price = sum(price * i for i in range(1, count + 1))
    if total_price <= money:
        return 0
    
    return total_price - money
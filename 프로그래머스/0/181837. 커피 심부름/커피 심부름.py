MENU_LIST = {
    'americano': 4_500,
    'cafelatte': 5_000,
}

def solution(order):
    total_price = 0
    for menu in order:
        menu_name = menu.replace("ice", "").replace("hot", "")
        if menu_name in MENU_LIST:
            total_price += MENU_LIST[menu_name]
        elif menu_name == "anything":
            total_price += MENU_LIST["americano"]
    
    return total_price
menu = {"Pizza": 1.99, "Soda": 0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def add_item(item: str, price: int) -> None:
    menu[item] = price

item = input("What item would you like to add to the menu?\n")
price = input("What price would you like to assign to the item?\n")
add_item(item, price)

print(menu)

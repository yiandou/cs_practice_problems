groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "dr. pepper", "mountain dew"]

while True:
    print(groceries)
    removed = input("Input grocery to remove. Type STOP to stop.\n")
    
    if removed == "STOP":
        break;
    
    groceries.remove(removed)

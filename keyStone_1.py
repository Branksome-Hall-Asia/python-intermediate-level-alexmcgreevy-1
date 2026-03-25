# KEYSTONE 01: RPG INVENTORY MANAGER
# Goal: Use functions and lists to manage items.

inventory = ["Wood", "Stone"]

def add_item():
    item = input("What would you like to add? ")
    inventory.append(item)
    print(f"{item} added!")

def view_inventory():
    print("\n--- Current Inventory ---")
    for item in inventory:
        print(f"- {item}")

# 1. Create a function 'remove_item()'.
# 2. Create a 'while True' loop that asks the user to (A)dd, (V)iew, or (R)emove.
# 3. Stop the loop if they type 'Exit'.

# WRITE YOUR CODE BELOW:

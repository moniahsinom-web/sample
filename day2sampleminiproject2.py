# Inventory Management System

# Dictionary to store inventory
inventory = {}

# Function to add a new item or update stock
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"Updated {item_name}: now {inventory[item_name]} in stock.")
    else:
        inventory[item_name] = quantity
        print(f"Added new item: {item_name} with {quantity} in stock.")

# Function to check stock of an item
def check_stock(item_name):
    if item_name in inventory:
        print(f"{item_name} has {inventory[item_name]} units in stock.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to display the entire inventory
def display_inventory():
    if inventory:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity}")
    else:
        print("Inventory is empty.")

# Sample usage
add_item("Apples", 10)
add_item("Oranges", 20)
add_item("Apples", 5)
check_stock("Apples")
check_stock("Bananas")
display_inventory()

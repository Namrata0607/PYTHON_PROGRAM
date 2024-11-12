# Inventory represented as a dictionary
inventory = {
    "Laptop": {"price": 1000, "stock": 5, "category": "Electronics"},
    "Phone": {"price": 500, "stock": 10, "category": "Electronics"},
    "Shampoo": {"price": 50, "stock": 50, "category": "Cosmetics"},
    "Pen": {"price": 10, "stock": 100, "category": "Stationary"},
    "Pencil": {"price": 15, "stock": 150, "category": "Stationary"},

}

# Function to add a new product to the inventory
def add_product(name, price, stock, category):
    if name in inventory:
        print(f"{name} already exists in the inventory.")
    else:
        inventory[name] = {"price": price, "stock": stock, "category": category}
        print(f"{name} has been added to the inventory.")

# Function to update the stock of a product
def update_stock(name, new_stock):
    if name in inventory:
        inventory[name]["stock"] = new_stock
        print(f"Updated stock for {name} to {new_stock}.")
    else:
        print(f"{name} does not exist in the inventory.")

# Function to list all products in a specific category
def list_products_by_category(category):
    print(f"Products in category '{category}':")
    for product, attributes in inventory.items():
        if attributes["category"] == category:
            print(f" {product}: ${attributes['price']}, Stock: {attributes['stock']}")

# Function to display the total value of all items in stock
def total_stock_value():
    total_value = 0
    for product, attributes in inventory.items():
        total_value += attributes["price"] * attributes["stock"]
    print(f"Total value of all items in stock: ${total_value}")

# Example usage of the functions
add_product("Tablet", 300, 7, "Electronics")
update_stock("Shampoo", 60)
list_products_by_category("Electronics")
total_stock_value()

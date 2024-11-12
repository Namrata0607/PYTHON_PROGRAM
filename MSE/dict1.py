inventory = {
    "Laptop": {"price": 1000, "stock": 5, "category": "Electronics"},
    "Phone": {"price": 500, "stock": 10, "category": "Electronics"},
    "Shampoo": {"price": 5, "stock": 50, "category": "Cosmetics"},
}

def addProduct():
    name = input("Enter product name: ")
    if inventory.get(name):                                 
        print(name + " already exists in the inventory.")
    else:
        price = float(input("Enter price for " + name + ": "))
        stock = int(input("Enter stock for " + name + ": "))
        category = input("Enter category for " + name + ": ")
        inventory.update({name: {"price": price, "stock": stock, "category": category}})
        print(name + " has been added to the inventory.\n")

def updateStock():
    name = input("Enter product name to update stock: ")
    if inventory.get(name):                                 #get()
            new_stock = int(input("Enter new stock for " + name + ": "))
            inventory[name].update({"stock": new_stock})
            print("Updated stock for " + name + " to " + str(new_stock) + "\n")
    else:
        print(name + " does not exist in the inventory.")

def productListByCat():
    category = input("Enter category to list products: ")
    print("Products in category '" + category + "':")
    found = False
    for product, attributes in inventory.items():
        if attributes.get("category") == category:          #items()
            found = True
            print("- " + product + ":" + str(attributes.get("price")) + ", Stock: " + str(attributes.get("stock")))
    if not found:
        print("No products found in category '" + category + "\n")

def totalStock():
    total_value = 0
    for product, attributes in inventory.items():          #items()
        total_value += attributes.get("price") * attributes.get("stock")
    print("Total value of all items in stock: " + str(total_value))

def displayProducts():
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Current products in the inventory:")
        for product, details in inventory.items():          #items()
            print("\nProduct: " + product)
            print("Price: " + str(details.get('price')))
            print("Stock: " + str(details.get('stock')))
            print("Category: " + details.get('category'))

def main():
    while True:
        print("1. Add a new product")
        print("2. Update stock of a product")
        print("3. List products by category")
        print("4. Display total value of all items in stock")
        print("5. Display all products in inventory")
        print("6. Exit")
        
        choice = input("Enter a choice: ")
        
        if choice == "1":
            addProduct()
        elif choice == "2":
            updateStock()
        elif choice == "3":
            productListByCat()
        elif choice == "4":
            totalStock()
        elif choice == "5":
            displayProducts()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice")

main()

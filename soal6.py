products = {}

while True:
    command = input("Enter command:\n 1-add\n 2-sell\n 3-search\n 4-show\n 5-report\n 6-exit\n ")

    if command == "add":
        name = input("Product name: ")
        quantity = int(input("Quantity: "))

        if name in products:
            products[name] = products[name] + quantity
        else:
            products[name] = quantity

    elif command == "sell":
        name = input("Product name: ")
        quantity = int(input("Quantity: "))

        if name not in products:
            print("Product not found")

        elif products[name] < quantity:
            print("Not enough inventory")

        else:
            products[name] = products[name] - quantity

            if products[name] == 0:
                del products[name]

    elif command == "search":
        name = input("Product name: ")

        if name in products:
            print("Inventory:", products[name])
        else:
            print("Product not found")

    elif command == "show":
        for name, quantity in products.items():
            print(f"{name} - {quantity}")

    elif command == "save":
        with open("inventory.txt", "w") as file:
            for name, quantity in products.items():
                file.write(f"{name} - {quantity}\n")

        print("Inventory saved")

    elif command == "report":
        print("Number of products:", len(products))
        print("Total inventory:", sum(products.values()))

        if len(products) > 0:
            max_product = max(products, key=products.get)
            min_product = min(products, key=products.get)

            print(f"Most inventory: {max_product}")
            print(f"Least inventory: {min_product}")

    elif command == "exit":
        break

    else:
        print("Invalid command")
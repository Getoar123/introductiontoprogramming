# Project 5 — Mini Shopping Cart
# Author: Getoar Sopa

menu = {
    1: ("Apple", 0.50),
    2: ("Banana", 0.30),
    3: ("Milk", 1.20),
    4: ("Bread", 2.00),
}

cart = {}
total = 0.0

# Display menu
print("--- Shop Menu ---")

for key, (name, price) in menu.items():
    print(f"{key}. {name:<7} ${price:.2f}")

print("5. Done")

# Shopping loop
while True:
    choice = int(input("Choose an item (1-5): "))

    if choice == 5:
        break

    if choice not in menu:
        print("Invalid choice. Try again.")
        continue

    item_name, price = menu[choice]

    # Add item to cart
    if item_name in cart:
        cart[item_name] += 1
    else:
        cart[item_name] = 1

    total += price

    print(f"Added {item_name}. Total: ${total:.2f}")

# Print receipt
print("\n--- Receipt ---")

for item, quantity in cart.items():
    for key, (name, price) in menu.items():
        if name == item:
            item_price = price
            break

    print(f"{item:<7} x{quantity}   ${item_price * quantity:.2f}")

print("---------------------")
print(f"Total: ${total:.2f}")
print("Thank you!")

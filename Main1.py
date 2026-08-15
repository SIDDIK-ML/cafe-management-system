Menu = {
    "Pizza": 150,
    "Burger": 100,
    "Sandwich": 100,
    "Pasta": 80,
    "French fries": 60,
    "Milkshake": 80,
    "Cold Coffee": 50
}

order_total = 0
order = []

while True:

    item = input("\nEnter the item you want to order: ").title()

    if item in Menu:
        quantity = int(input("Enter quantity: "))

        total = Menu[item] * quantity
        order.append((item, quantity, total))
        order_total += total

        print(f"{item} x {quantity} added.")
        print(f"Item total: ₹{total}")

    else:
        print("Sorry! Item not available.")

    another = input("Do you want to order anything else? (Yes/No): ")

    if another.lower() == "no":
        break

print("Summary of your orders")
print("\n========== ORDER SUMMARY ==========")

for item, quantity, total in order:
    print(f"{item} x {quantity} = ₹{total}")

print("-----------------------------------")
print(f"Total Amount: ₹{order_total}")
print("===================================")
print("Thank you for your order!")

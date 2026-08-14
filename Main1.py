# #Define Menu of Cafe 
# Menu = {
#     "Pizza" : 150,
#     "Burger" : 100,
#     "Sandwich" : 100,
#     "Pasta" : 80,
#     "French fries" : 60,
#     "Milkshake" : 80,
#     "Cold Coffee" : 50
# }

# #greet
# print("Welcome to Python Cafe!")
# print("Pizza : Rs150\nBurger : Rs100\nSandwich : Rs100\nPasta : Rs80\nFrench fries : Rs60\nMilkshake : Rs80\nCold Coffee : Rs50 ")

# Order_total = 0
# item_1 = input("Enter the name of item you want to order = ")
# if item_1 in Menu :
#     Order_total += Menu[item_1]
#     print(f"Your item {item_1} has been added to your order")

# else:
#     print(f"ordered item {item_1} is not avaliable yet!")

# Another_item = input("Do you want to order anything else? (Yes/No)")

# if Another_item == "Yes":
#     item_2 = input("Enter the name of item you want to order = ")
#     if item_2 in Menu :
#         Order_total += Menu[item_2]
#         print(f"Your item {item_2} has been added to your order")
        
#     else:
#             print(f"ordered item {item_2} is not avaliable yet!")
            

# print(f"The total amountof items to pay is {Order_total}")
#         #    
# """Advance"""
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

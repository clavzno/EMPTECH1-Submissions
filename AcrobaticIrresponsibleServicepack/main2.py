price = float(input("Enter price of item to purchase: "))
quantity = int(input("Enter quantity: "))
name = input("Enter your name: ")
cash = float(input("Enter cash payment amount: "))
print("\nHi, ", name)
print("Total Purchase: ", quantity, " x ", price, " = ", price * quantity )
print("Cash Payment: ", cash)
print("Change: ", cash - price * quantity )
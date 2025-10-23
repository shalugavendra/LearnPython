# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy ? ")
price = float(input(f"What's the Price for {item} ?"))
quantity = int(input("How many would you like ? "))

total = price * quantity

print(f"You have bought {quantity} {item} for a total of {total}")
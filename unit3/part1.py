# Part 1: Restaurant Meal Calculator

# Get the food charge from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate tip (18%)
tip = food_charge * 0.18

# Calculate sales tax (7%)
sales_tax = food_charge * 0.07

# Calculate total
total = food_charge + tip + sales_tax

# Display the results
print(f"\nFood Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")


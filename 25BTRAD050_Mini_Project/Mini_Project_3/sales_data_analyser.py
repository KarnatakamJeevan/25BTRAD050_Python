products = {}

while True:
print("\n--- Sales Data Analyser ---")
print("1. Add Product")
print("2. Update Sales")
print("3. Display Sales")
print("4. Total Revenue")
print("5. Highest Selling Product")
print("6. Exit")

choice = input("Enter choice: ")

if choice == "1":
name = input("Enter product name: ")

if name not in products:
quantity = int(input("Enter quantity sold: "))
price = float(input("Enter price per item: "))

if quantity >= 0 and price >= 0:
products[name] = {
"quantity": quantity,
"price": price
}
print("Product added successfully!")
else:
print("Quantity and price cannot be negative!")
else:
print("Product already exists!")

elif choice == "2":
name = input("Enter product name: ")

if name in products:
quantity = int(input("Enter new quantity sold: "))

if quantity >= 0:

products[name]["quantity"] = quantity
print("Sales updated successfully!")
else:
print("Quantity cannot be negative!")
else:
print("Product not found!")

elif choice == "3":
print("\nProduct\t\tQuantity\tRevenue")

for name, details in products.items():
revenue = details["quantity"] * details["price"]

print(name, "\t\t", details["quantity"],
"\t\t", round(revenue, 2))

elif choice == "4":
total = 0

for details in products.values():
total += details["quantity"] * details["price"]

print("Total Revenue:", round(total, 2))

elif choice == "5":
if products:
highest = max(
products,

key=lambda name: products[name]["quantity"]
)

print("Highest Selling Product:", highest)
print("Quantity Sold:", products[highest]["quantity"])
else:
print("No products available!")

elif choice == "6":
print("Exiting program...")
break

else:
print("Invalid choice! Try again.")

# Contact Book Program
# Data structure: a dictionary maps each contact name to a list [phone,
email].

contacts = {}

def add_contact(name, phone, email):
if name in contacts:

print(f"Contact '{name}' already exists.")
else:
contacts[name] = [phone, email]
print(f"Contact '{name}' added successfully.")

def search_contact(name):
if name in contacts:
print(f"Name: {name} | Phone: {contacts[name][0]} | Email:
{contacts[name][1]}")
else:
print(f"Contact '{name}' not found.")

def update_contact(name, phone, email):
if name in contacts:
contacts[name] = [phone, email]
print(f"Contact '{name}' updated successfully.")
else:
print(f"Contact '{name}' not found.")

def delete_contact(name):
if name in contacts:
del contacts[name]
print(f"Contact '{name}' deleted successfully.")
else:
print(f"Contact '{name}' not found.")

def display_contacts():
if not contacts:
print("The contact book is empty.")
else:
print("\n--- Contact List ---")
for name, details in contacts.items():
print(f"Name: {name} | Phone: {details[0]} | Email:
{details[1]}")

# Example Usage (Testing)
add_contact("Ravi", "9876543210", "Ravi@email.com")
add_contact("Tom", "1234567890", "tom@email.com")
add_contact("Sunil;", "0000000000", "sun@email.com") # duplicate
check
search_contact("Ravi")
search_contact("Bob") # not found check
update_contact("Ravi", "9999999999", "Ravi_new@email.com")
display_contacts()
delete_contact("Bob")
delete_contact("Bob") # already deleted check
display_contacts()

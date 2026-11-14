class Item:
"""Base class demonstrating inheritance foundations."""

def __init__(self, title, unique_id):
self.title = title
self.unique_id = unique_id
self.is_available = True

class Book(Item):

"""Subclass inheriting from Item."""

def __init__(self, title, unique_id, author, isbn):
super().__init__(title, unique_id)
self.author = author
self.isbn = isbn

class Library:
def __init__(self):
self.catalog = {}

def add_book(self, book):
self.catalog[book.unique_id] = book
print(f"Added book to catalog: '{book.title}' by {book.author}")

def issue_book(self, unique_id, student_name):
if unique_id not in self.catalog:

print("Error: Book code not found in directory.")
return
book = self.catalog[unique_id]

# Check book availability condition
if not book.is_available:
print(f"Unavailable: '{book.title}' is already checked out.")
return
book.is_available = False
print(f"Success: '{book.title}' checked out to {student_name}.")

def return_book(self, unique_id):
if unique_id not in self.catalog:
print("Error: Book code not found in directory.")
return
book = self.catalog[unique_id]

if book.is_available:

print(f"Notice: '{book.title}' is already present in the library.")
return
book.is_available = True
print(f"Success: '{book.title}' has been successfully returned.")

# --- Test Cases & Simulation ---
print("\n=== Library Management Simulation ===")
lib = Library()

# Instantiate books
b1 = Book("Python Crash Course", "B01", "Eric Matthes", "978-1593279288")
b2 = Book("Introduction to Algorithms", "B02", "CLRS", "978-0262046305")

# Build inventory
lib.add_book(b1)
lib.add_book(b2)

# Simulate issue/return transactions
print("\n--- Testing Transactions ---")
lib.issue_book("B01", "Divya")
lib.issue_book("B01", "Rohit") # Test double-issue block
lib.return_book("B01")
lib.issue_book("B01", "Rohit") # Test issue after return

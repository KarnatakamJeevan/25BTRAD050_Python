import os

FILE_NAME = "students.txt"

def add_student(roll_no, name, course):
# Input validation
if not roll_no or not name or not course:
print("Invalid Input: All fields are required.")
return
with open(FILE_NAME, "a") as f:
f.write(f"{roll_no},{name},{course}\n")
print(f"Record for Roll No {roll_no} saved successfully.")

def search_student(roll_no):
if not os.path.exists(FILE_NAME):
print("No records found.")
return
with open(FILE_NAME, "r") as f:
for line in f:

r_no, name, course = line.strip().split(",")
if r_no == str(roll_no):
print(f"\nFound Student -> Roll No: {r_no} | Name: {name} | Course: {course}")
return
print(f"Student with Roll No {roll_no} not found.")

def update_student(roll_no, new_name, new_course):
if not os.path.exists(FILE_NAME):
print("No records to update.")
return
updated = False
lines = []
with open(FILE_NAME, "r") as f:
lines = f.readlines()
with open(FILE_NAME, "w") as f:
for line in lines:
r_no, name, course = line.strip().split(",")

if r_no == str(roll_no):
f.write(f"{roll_no},{new_name},{new_course}\n")
updated = True
else:
f.write(line)
if updated:
print(f"Roll No {roll_no} updated successfully.")
else:
print(f"Roll No {roll_no} not found.")

def display_all():
if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
print("Database is empty.")
return
print("\n--- Student Database Records ---")
with open(FILE_NAME, "r") as f:
for line in f:

r_no, name, course = line.strip().split(",")
print(f"Roll No: {r_no} | Name: {name} | Course: {course}")

# Execution / Testing
if os.path.exists(FILE_NAME):
os.remove(FILE_NAME) # Reset local test run

add_student("101", "Karthik", "Computer Science")
add_student("102", "Sanjana", "Data Science")
display_all()
search_student("101")
update_student("101", "Karthikeya", "AI & Robotics")

students = {}

while True:
print("\n--- Student Attendance Management ---")
print("1. Add Student")
print("2. Update Attendance")
print("3. Display Attendance")
print("4. Check Shortage")
print("5. Exit")

choice = input("Enter choice: ")

if choice == "1":
name = input("Enter student name: ")

if name not in students:
students[name] = []
print("Student added successfully!")
else:

print("Student already exists!")

elif choice == "2":
name = input("Enter student name: ")

if name in students:
status = input("Enter P for Present or A for Absent: ").upper()

if status == "P" or status == "A":
students[name].append(status)
print("Attendance updated successfully!")
else:
print("Invalid attendance status!")
else:
print("Student not found!")

elif choice == "3":
print("\nName\t\tAttendance\tPercentage")

for name, records in students.items():
total = len(records)
present = records.count("P")

if total > 0:
percentage = (present / total) * 100
else:
percentage = 0

print(name, "\t\t", records, "\t", round(percentage, 2), "%")

elif choice == "4":
limit = float(input("Enter attendance threshold: "))

for name, records in students.items():
total = len(records)

if total > 0:
percentage = (records.count("P") / total) * 100

if percentage < limit:
print(name, "has low attendance:", round(percentage, 2), "%")

elif choice == "5":
print("Exiting program...")
break

else:
print("Invalid choice! Try again.")

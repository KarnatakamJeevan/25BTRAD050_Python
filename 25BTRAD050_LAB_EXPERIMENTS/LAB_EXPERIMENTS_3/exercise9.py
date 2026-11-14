# Student Grading System Program

student_marks = {
"Arjun": 88,
"Lakshmi": 95,
"Vikram": 72,
"Priya": 60,
"Harish": 45,
}

def calculate_grade(marks):
if marks >= 90:
return "A+"
elif marks >= 80:
return "A"
elif marks >= 70:
return "B"
elif marks >= 60:
return "C"
elif marks >= 50:
return "D"
else:
return "F"

def display_results(records):
print("\n--- Student Grading Results ---")
for name, marks in records.items():
grade = calculate_grade(marks)
print(f"Student: {name} | Marks: {marks} | Grade: {grade}")

# Test Cases & Execution
display_results(student_marks)

# Add a new test student
student_marks["Ananya"] = 82
print("\nAfter adding Ananya:")
display_results(student_marks)

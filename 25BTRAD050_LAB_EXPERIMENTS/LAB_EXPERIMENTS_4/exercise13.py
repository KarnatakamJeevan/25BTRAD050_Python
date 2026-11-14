import csv

def generate_sample_payroll_csv(filename="employees.csv"):
"""Generates a base spreadsheet file for the program to parse."""
headers = ["EmpID", "Name", "BaseSalary", "Allowances"]
data = [
["E001", "Rajesh", "50000", "12000"],
["E002", "Meenakshi", "75000", "15000"],
["E003", "Suresh", "42000", "8000"],
]
with open(filename, "w", newline="") as f:

writer = csv.writer(f)
writer.writerow(headers)
writer.writerows(data)

def process_payroll(filename="employees.csv"):
# Constants for calculation logic
TAX_RATE = 0.12 # 12% baseline income tax
PROVIDENT_FUND_RATE = 0.05 # 5% PF contribution
try:
with open(filename, mode="r") as f:
reader = csv.DictReader(f)
print(
f"\n{'Emp ID':<8} | {'Name':<15} | {'Gross Salary':<12} |"
f" {'Deductions':<12} | {'Net Pay':<12}"
)
print("-" * 65)
total_company_payout = 0
for row in reader:
# Data validation and parsing
emp_id = row["EmpID"]
name = row["Name"]
base = float(row["BaseSalary"])
allowance = float(row["Allowances"])
# Payroll math formulas
gross_salary = base + allowance
tax_deduction = gross_salary * TAX_RATE
pf_deduction = gross_salary * PROVIDENT_FUND_RATE
total_deductions = tax_deduction + pf_deduction
net_pay = gross_salary - total_deductions
total_company_payout += net_pay
print(
f"{emp_id:<8} | {name:<15} | ₹{gross_salary:<11.2f} |"
f" ₹{total_deductions:<11.2f} | ₹{net_pay:<11.2f}"
)
print("-" * 65)
print(f"Total Bank Disbursal Amount: ₹{total_company_payout:.2f}")

except FileNotFoundError:
print(f"Payroll target storage source file '{filename}' was not found.")

# Execution / Testing
generate_sample_payroll_csv()
process_payroll()

def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

print("1. Centimetre to Inches")
print("2. Inches to Centimetre")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    cm = float(input("Enter centimetres: "))
    print("Inches =", cm_to_inches(cm))
elif choice == 2:
    inches = float(input("Enter inches: "))
    print("Centimetres =", inches_to_cm(inches))
else:
    print("Invalid choice")

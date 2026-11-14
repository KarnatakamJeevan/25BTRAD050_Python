class BankAccount:
def __init__(self, account_holder, account_number, initial_balance=0.0):
self.account_holder = account_holder
self.account_number = account_number
# Encapsulation: Private attribute prefixed with double underscore
self.__balance = float(initial_balance)

def deposit(self, amount):
# Transaction validation: Ensure positive amounts
if amount <= 0:

print("Transaction Denied: Deposit amount must be positive.")
return False

self.__balance += amount
print(f"Deposited: ₹{amount:.2f} | New Balance: ₹{self.__balance:.2f}")
return True

def withdraw(self, amount):
# Transaction validation: Ensure positive amounts
if amount <= 0:
print("Transaction Denied: Withdrawal amount must be positive.")
return False

# Transaction condition: Check for insufficient funds
if amount > self.__balance:
print(f"Transaction Denied: Insufficient balance. Available: ₹{self.__balance:.2f}")
return False

self.__balance -= amount
print(f"Withdrawn: ₹{amount:.2f} | Remaining Balance: ₹{self.__balance:.2f}")
return True

def check_balance(self):
print(f"Account Holder: {self.account_holder} | Current Balance: ₹{self.__balance:.2f}")
return self.__balance

# --- Test Cases & Simulation ---
print("=== Banking Simulation ===")
# Create a new account
account = BankAccount("Vishnu", "ACC12345", 8000.0)

# 1. Check Initial Balance
account.check_balance()

# 2. Test Valid Deposit & Withdrawal
account.deposit(2500.0)
account.withdraw(3000.0)

# 3. Test Invalid Transactions (Negative values)
account.deposit(-700)
account.withdraw(-200)

# 4. Test Overdraft / Insufficient Balance
account.withdraw(15000.0)

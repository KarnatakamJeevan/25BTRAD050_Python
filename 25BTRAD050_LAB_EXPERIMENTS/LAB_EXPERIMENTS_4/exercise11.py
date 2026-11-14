import os

def generate_sample_log(filename="app.log"):
"""Helper function to create a dummy log file for testing."""

sample_data = """2026-11-05 08:00:12 INFO User logged in successfully.
2026-11-05 08:05:43 WARNING Disk usage is at 85%.
2026-11-05 08:06:11 ERROR Failed to connect to the database.
2026-11-05 08:10:00 INFO Page request processed in 12ms.
2026-11-05 08:15:22 ERROR Payment gateway timeout.
2026-11-05 08:20:05 INFO Session cleared for idle user."""
with open(filename, "w") as f:
f.write(sample_data.strip())

def analyze_log_file(filename="app.log"):
keywords = {"ERROR": 0, "WARNING": 0, "INFO": 0}

# Computational Logic / Exception Handling
try:
if os.path.exists(filename) and os.path.getsize(filename) == 0:
print(f"File '{filename}' is empty.")
return keywords

with open(filename, "r") as file:
for line in file:
# Check for keywords in each log line
for key in keywords:
if key in line:
keywords[key] += 1

# Display Results
print(f"\n--- Log Summary for '{filename}' ---")
for key, count in keywords.items():
print(f"{key}: {count} occurrences")
return keywords

except FileNotFoundError:
print(f"Error: The file '{filename}' does not exist.")
except IOError:
print(f"Error: Could not read the file '{filename}'.")

# Execution / Testing
generate_sample_log() # Creates app.log automatically
analyze_log_file("app.log")
analyze_log_file("missing_file.log") # Tests exception handling

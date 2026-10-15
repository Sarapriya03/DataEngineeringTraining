# JSON (Q24-32)

import json

# 24. Read employees.json.
with open("employees.json") as f:
    employees = json.load(f)

# 25. Display all employee names.
print("Names:", [e["name"] for e in employees])

# 26. Find employees earning above 75000.
print("Salary > 75000:", [e["name"] for e in employees if e["salary"] > 75000])

# 27. Display employees knowing Python.
print("Know Python:", [e["name"] for e in employees if "Python" in e["skills"]])

# 28. Display employee name and performance rating.
for e in employees:
    print(e["name"], e["performance"]["rating"])

# 29. Find employees whose rating exceeds 4.5.
print("Rating > 4.5:", [e["name"] for e in employees if e["performance"]["rating"] > 4.5])

# 30. Sort employees by rating descending.
for e in sorted(employees, key=lambda e: e["performance"]["rating"], reverse=True):
    print(e["name"], e["performance"]["rating"])

# 31. Add one skill to employee 303.
for e in employees:
    if e["employee_id"] == 303:
        e["skills"].append("Python")

# 32. Save the modified JSON.
with open("employees_updated.json", "w") as f:
    json.dump(employees, f, indent=2)
print("Saved employees_updated.json")
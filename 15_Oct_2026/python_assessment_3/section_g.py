# Section G - JSON Processing (Q61-74)
# Using staff.json
import json

# 61. Read JSON into Python.
with open("staff.json") as f:
    staff = json.load(f)

# 62. Check the datatype of the returned object.
print("Type:", type(staff))

# 63. Display all staff names.
print("Names:", [s["name"] for s in staff])

# 64. Display employees from Operations.
print("Operations:", [s["name"] for s in staff if s["department"] == "Operations"])

# 65. Display employees whose salary exceeds ₹75,000.
print("Salary > 75000:", [s["name"] for s in staff if s["salary"] > 75000])

# 66. Find employees having Python in their skills.
print("Python:", [s["name"] for s in staff if "Python" in s["skills"]])

# 67. Display:Name,Rating,Events Handled
for s in staff:
    print(s["name"], s["performance"]["rating"], s["performance"]["events_handled"])

# 68. Find staff whose performance rating exceeds 4.5.
print("Rating > 4.5:", [s["name"] for s in staff if s["performance"]["rating"] > 4.5])

# 69. Extract all skills into one list.
all_skills = [sk for s in staff for sk in s["skills"]]
print("All skills   :", all_skills)

# 70. Find unique skills.
print("Unique skills:", set(all_skills))

# 71. Sort employees by salary descending.
print("By salary desc:", [s["name"] for s in sorted(staff, key=lambda s: s["salary"], reverse=True)])

# 72. Sort employees by performance rating descending.
print("By rating desc:", [s["name"] for s in sorted(staff, key=lambda s: s["performance"]["rating"], reverse=True)])

# 73. Add "Pandas" to staff ID 503.
for s in staff:
    if s["staff_id"] == 503:
        s["skills"].append("Pandas")

# 74. Save the modified JSON as:staff_updated.json
with open("staff_updated.json", "w") as f:
    json.dump(staff, f, indent=2)
print("Saved staff_updated.json")
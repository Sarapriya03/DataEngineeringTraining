import json

# --- Task 1: Read the JSON file into Python ---

with open("projects.json", "r") as file:
    projects = json.load(file)

# --- Task 2: Check the datatype of the returned object ---

print(f"Task 2: Datatype of parsed JSON object: {type(projects)}")

# --- Task 3: Display all project names ---

print("\nTask 3: Project Names:")
for p in projects:
    print(p["project_name"])

# --- Task 4: Display projects having a budget above ₹4,00,000 ---

print("\nTask 4: Projects with budget > ₹4,00,000:")
for p in projects:
    if p["budget"] > 400000:
        print(f"- {p['project_name']} (₹{p['budget']:,})")

# --- Task 5: Display projects that use Python ---

print("\nTask 5: Projects using Python:")
for p in projects:
    if "Python" in p["technologies"]:
        print(f"- {p['project_name']}")

# --- Task 6: Calculate the total budget of all projects ---

total_budget = 0
for p in projects:
    total_budget += p["budget"]
print(f"\nTask 6: Total Budget of all projects: ₹{total_budget:,}")

# --- Task 7: Extract all technologies into one Python list ---

all_technologies = []
for p in projects:
    for tech in p["technologies"]:
        all_technologies.append(tech)
print(f"\nTask 7: All Technologies List: {all_technologies}")

# --- Task 8: Find the unique technologies ---

# Creating a set drops duplicates automatically
unique_techs = set(all_technologies)
print(f"Task 8: Unique Technologies: {unique_techs}")

# --- Task 9: Display every team member's details ---

print("\nTask 9: All Team Members:")
for p in projects:
    for member in p["team"]:
        print(f"Name: {member['name']}, Role: {member['role']}, Experience: {member['experience']} years")

# --- Task 10: Display team members having more than 3 years of experience ---

print("\nTask 10: Team Members with > 3 years experience:")
for p in projects:
    for member in p["team"]:
        if member["experience"] > 3:
            print(f"- {member['name']} ({member['experience']} years)")

# --- Task 11: Find the total number of team members across all projects ---

total_members = 0
for p in projects:
    total_members += len(p["team"])
print(f"\nTask 11: Total Team Members Cross-Project: {total_members}")

# --- Task 12: Sort projects by budget from highest to lowest ---

print("\nTask 12: Projects Sorted by Budget (Highest to Lowest):")
sorted_by_budget = sorted(projects, key=lambda p: p["budget"], reverse=True)
for p in sorted_by_budget:
    print(f"- {p['project_name']}: ₹{p['budget']:,}")

# --- Task 13: Sort projects alphabetically by project name ---

print("\nTask 13: Projects Sorted Alphabetically:")
sorted_by_name = sorted(projects, key=lambda p: p["project_name"])
for p in sorted_by_name:
    print(f"- {p['project_name']}")

# --- Task 14: Sort each project's team members based on experience ---

print("\nTask 14: Each Project's Team Members Sorted by Experience:")
for p in projects:
    print(f"Project: {p['project_name']}")
    # Sorting members of the current project loop
    sorted_team = sorted(p["team"], key=lambda m: m["experience"])
    for member in sorted_team:
        print(f"  * {member['name']} - {member['experience']} years")

student = {
    "name": "Maaz",
    "age": 20,
    "branch": "CSE",
    "marks": 85
}

print("Student:", student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])

student["marks"] = 90

print("Updated marks:", student["marks"])

student["city"] = "Dhanbad"

print("Updated student:", student)
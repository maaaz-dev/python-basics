students = {
    "Maaz": 85,
    "Rahul": 78,
    "Aman": 92,
    "Rohit": 67
}

print("Student Marks:", students)

name = input("Enter student name: ")

if name in students:
    print(name, "scored", students[name])
else:
    print("Student not found.")
# Using lambda with sorted()

students = [("Aida", 90), ("Dana", 75), ("Ali", 85)]

# Sort by score
sorted_students = sorted(students, key=lambda x: x[1])
print(*sorted_students)
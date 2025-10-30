# Objective: To calculate the average grade of a list of students 
# and determine the highest and lowest scores.

# Step 1: Create a dictionary to store student names and their grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 67
}

# Step 2: Extract all grades into a list
grades = list(students.values())

# Step 3: Calculate the average grade
average_grade = sum(grades) / len(grades)

# Step 4: Find the highest and lowest scores
highest_score = max(grades)
lowest_score = min(grades)

# Step 5: Find which students have the highest and lowest scores
highest_student = [name for name, grade in students.items() if grade == highest_score]
lowest_student = [name for name, grade in students.items() if grade == lowest_score]

# Step 6: Display results
print("=== Student Grade Report ===")
print(f"Average Grade: {average_grade:.2f}")
print(f"Highest Score: {highest_score} ({', '.join(highest_student)})")
print(f"Lowest Score: {lowest_score} ({', '.join(lowest_student)})")

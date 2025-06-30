def calculate_percentage(student_name, *marks):
    # Calculate total possible marks (assuming each subject is out of 100)
    total_marks = len(marks) * 100

    # Initialize total marks obtained
    total_marks_obtained = 0

    # Sum up all the marks obtained
    for mark in marks:
        total_marks_obtained += mark

    # Calculate percentage
    percentage = (total_marks_obtained / total_marks) * 100

    # Return both the student's name and calculated percentage
    return student_name, percentage

# Function call with student name and marks in different subjects
name, percentage = calculate_percentage('Zahid', 10, 20, 56, 40, 60)

# Display the result in a user-friendly format
print(f"{name} has scored {percentage}% in the examination.")

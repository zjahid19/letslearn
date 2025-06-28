"""
Get user input for student marks (out of 100) for all 6 subjects.
Calculate the percentage and determine the grade based on the percentage:
- Percentage greater than or equal to 75 → A+
- Percentage greater than or equal to 60 and less than 75 → A
- Percentage greater than or equal to 50 and less than 60 → B
- Percentage greater than or equal to 35 and less than 50 → C
- Percentage less than 35 → Needs Improvement
"""

# Get the user input for all subjects
english_marks = int(input('Enter English subject marks out of 100: '))
hindi_marks = int(input('Enter Hindi subject marks out of 100: '))
maths_marks = int(input('Enter Maths subject marks out of 100: '))
biology_marks = int(input('Enter Biology subject marks out of 100: '))
chemistry_marks = int(input('Enter Chemistry subject marks out of 100: '))
biology_marks = int(input('Enter Biology subject marks out of 100: '))

# total marks for each subject 
total_marks = 600

# total marks obtained 
total_marks_obtained = english_marks + hindi_marks + maths_marks + biology_marks + chemistry_marks + biology_marks

# calculate the percentage using (marks optained / total marks) * 100
percentage = (total_marks_obtained/total_marks) * 100 

# Decide grade on the basis of percentage 
if percentage >= 75:
    print('Student got A+ grade')
elif percentage >= 60 and percentage <= 75:
    print('Student got A grade')
elif percentage >= 50 and percentage <= 60:
    print('Student got B grade')
elif percentage >= 35 and percentage <= 50:
    print('Student got C grade')
else:
    print('student failed in exam')

print('Program Completed successfully')
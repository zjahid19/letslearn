# Function to display employee information using flexible keyword arguments
def employee_info(**kwargs):
    print("--------- Employee Profile ---------")

    # Loop through each key-value pair and print in a formatted way
    for key, value in kwargs.items():
        # Capitalize the key and handle list values (like skills) cleanly
        if isinstance(value, list):
            print(f"{key.capitalize()}: {', '.join(value)}")
        else:
            print(f"{key.capitalize()}: {value}")

    print('----------------------------------------\n')


# First employee record
employee_info(
    name='Anup',
    salary=50000,
    location='Chennai',
    is_permanant=True
)

# Second employee record with additional fields
employee_info(
    name='Shekhar',
    location='Bangalore',
    is_permanant=True,
    yearly_bonus=50000,
    skills=['SQL', 'Python', 'Data Engineering']
)

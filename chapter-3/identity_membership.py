# Setup variables
list_numbers = [10, 20, 50, 100]
tuple_colors = ('red', 'green', 'blue')
str_message = "Hello Python"
x = 50
y = 50
z = 100

# Membership operators (in, not in)
in_result = (x in list_numbers)
print('50 in [10, 20, 50, 100]?', in_result)  # True

not_in_result = ('yellow' not in tuple_colors)
print("'yellow' not in ('red','green','blue')?", not_in_result)  # True

string_check = ('Py' in str_message)
print("'Py' in 'Hello Python'?", string_check)  # True

# Identity operators (is, is not)
is_result = (x is y)
print('x is y (both 50)?', is_result)  # True

is_not_result = (x is not z)
print('x is not z (50 vs 100)?', is_not_result)  # True

# Special case with mutable objects
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

same_content = (list_a == list_b)
print('list_a == list_b?', same_content)  # True (value equality)

same_object = (list_a is list_b)
print('list_a is list_b?', same_object)  # False (different objects)

alias_check = (list_a is list_c)
print('list_a is list_c?', alias_check)  # True (same object)
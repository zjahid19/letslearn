# Integer Conversion
# String to integer
num_str = "123"
num_int = int(num_str)
print(f"String '{num_str}' to integer: {num_int} ({type(num_int)})")

# Float to integer (truncates decimal part)
num_float = 12.99
num_int = int(num_float)
print(f"Float {num_float} to integer: {num_int} ({type(num_int)})")

# Boolean to integer
bool_val = True
num_int = int(bool_val)
print(f"Boolean {bool_val} to integer: {num_int} ({type(num_int)})")

# Float Conversion
# String to float
num_str = "123.45"
num_float = float(num_str)
print(f"String '{num_str}' to float: {num_float} ({type(num_float)})")

# Integer to float
num_int = 100
num_float = float(num_int)
print(f"Integer {num_int} to float: {num_float} ({type(num_float)})")

# Boolean to float
bool_val = False
num_float = float(bool_val)
print(f"Boolean {bool_val} to float: {num_float} ({type(num_float)})")

# String Conversion
# Integer to string
num_int = 42
num_str = str(num_int)
print(f"Integer {num_int} to string: '{num_str}' ({type(num_str)})")

# Float to string
num_float = 3.14159
num_str = str(num_float)
print(f"Float {num_float} to string: '{num_str}' ({type(num_str)})")

# Boolean to string
bool_val = True
bool_str = str(bool_val)
print(f"Boolean {bool_val} to string: '{bool_str}' ({type(bool_str)})")

# List to string
my_list = [1, 2, 3]
list_str = str(my_list)
print(f"List {my_list} to string: '{list_str}' ({type(list_str)})")

# Boolean Conversion
# Integer to boolean
num_int = 1
bool_val = bool(num_int)
print(f"Integer {num_int} to boolean: {bool_val} ({type(bool_val)})")

num_int = 0
bool_val = bool(num_int)
print(f"Integer {num_int} to boolean: {bool_val} ({type(bool_val)})")

# String to boolean
text = "Hello"
bool_val = bool(text)
print(f"String '{text}' to boolean: {bool_val} ({type(bool_val)})")

empty_text = ""
bool_val = bool(empty_text)
print(f"Empty string to boolean: {bool_val} ({type(bool_val)})")

# List to boolean
my_list = [1, 2, 3]
bool_val = bool(my_list)
print(f"List {my_list} to boolean: {bool_val} ({type(bool_val)})")

empty_list = []
bool_val = bool(empty_list)
print(f"Empty list to boolean: {bool_val} ({type(bool_val)})")


# List Conversion
# String to list (splits characters)
text = "hello"
char_list = list(text)
print(f"String '{text}' to list: {char_list} ({type(char_list)})")

# Tuple to list
my_tuple = (1, 2, 3)
tuple_list = list(my_tuple)
print(f"Tuple {my_tuple} to list: {tuple_list} ({type(tuple_list)})")

# Set to list
my_set = {4, 5, 6}
set_list = list(my_set)
print(f"Set {my_set} to list: {set_list} ({type(set_list)})")
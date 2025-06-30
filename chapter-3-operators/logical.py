number_1 = 50
number_2 = 100

# Using expressions with AND operator
and_result = (number_1 < number_2) and (number_2 == 100)
print('(50 < 100) AND (100 == 100) result is:', and_result)  

# Using expressions with OR operator
or_result = (number_1 > number_2) or (number_2 != 50)
print('(50 > 100) OR (100 != 50) result is:', or_result)     

# Using expressions with NOT operator
not_result = not (number_1 == number_2)
print('NOT (50 == 100) result is:', not_result)             

# Combined logical operations
combined_result = (number_1 + 50 == number_2) and not (number_1 >= number_2)
print('(50+50 == 100) AND NOT (50 >= 100) result is:', combined_result) 

# More complex expression
complex_result = ((number_1 * 2) == number_2) or ((number_2 / 2) < number_1)
print('(50*2 == 100) OR (100/2 < 50) result is:', complex_result)      
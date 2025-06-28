# input any number
number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))
operator = input("Enter operator (+, -, *, /): ")

# perform operation on the basis of operator
if operator == '+':
    result = number_1 + number_2
    print('Addition operation result is : ',result)
elif operator == '-':
    result = number_1 - number_2
    print('Substraction operation result is : ',result)
elif operator == '*':
    result = number_1 * number_2
    print('Multiplication operation result is : ',result)
elif operator == '/':
    result = number_1 / number_2
    print('Division operation result is : ',result)
else:
    print('Invalid Operator')

print('Program Completed successfully')
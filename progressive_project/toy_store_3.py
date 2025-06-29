"""Add Few more Calculations"""

# Fixed price of each toy in INR
toy_price = 100

# Discunt Percentage
discount = 2

# Name of the customer
customer_name = input('Enter Customer Name : ')

# Number of toys purchased by the customer
quantity = input('Enter Quntity of toys purchased by customer: ')

# typecase quantity from string to integer
quantity = int(quantity)

# Calculate total amount spent by the customer
total_amount = toy_price * quantity

# 2% discount on total amount
discount_amount = (total_amount * discount) / 100

# total amount spend after deducting discount 
discounted_total_amount = total_amount - discount_amount

# Display the total amount spent by the customer on toys
print(f'Total Amount is {total_amount}')
print(f'Discount Amount is {discount_amount}')
print(f"\n{customer_name} spent a total on toys after {discount}% discount is {discounted_total_amount}")

"""Add Input function,typecase to get variables and f-string as well"""

# Fixed price of each toy in INR
toy_price = 100

# Name of the customer
customer_name = input('Enter Customer Name : ')

# Number of toys purchased by the customer
quantity = input('Enter Quntity of toys purchased by customer: ')

# typecase quantity from string to integer
quantity = int(quantity)

# Calculate total amount spent by the customer
total_amount = toy_price * quantity

# Display the total amount spent by the customer on toys
print(f"\n{customer_name} spent a total on toys is {total_amount}")

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

# Apply discount on the basis of quantity
if quantity < 5:
    discount = 2
elif quantity > 5 and quantity < 10:
    discount = 5
elif quantity > 10:
    discount = 10
else:
    discount = 0

# Apply Tax on purchase
if quantity > 50:
    product_tax = 2
else:
    product_tax = 0
 
# % discount on total amount
discount_amount = (total_amount * discount) / 100

# Apply Tax amount on total Amount
tax_amount = (total_amount * product_tax) / 100

# total amount spend after deducting discount 
discounted_total_amount = total_amount - discount_amount + tax_amount


# Display the total amount spent by the customer on toys
print('\n---------Welcome to toy store---------')
print(f'Total Amount is {total_amount}')
print(f'Discount Amount is -{discount_amount}')
print(f'Tax Amount is +{tax_amount}')
print(f"\n{customer_name} spent a total on toys after {discount}% discount is {discounted_total_amount}")

"""
Upgrading Store from Fixed Price Toys to Variable Price Toys
"""

# Toys cart to hold details of all toys purchased
toy_cart = []

# Get the name of the customer
customer_name = input('Enter Customer Name: ')

# Get number of different toys the customer wants to purchase
quantity = input('Enter number of different toys purchased by customer: ')
quantity = int(quantity)  # Convert quantity from string to integer

# Entering details for each toy (name, price, quantity)
for each_toy in range(quantity):
    print(f"\nEnter details for Toy #{each_toy + 1}:")
    toy_name = input("Toy Name: ")
    toy_price = float(input("Toy Price (INR): "))
    toy_qty = int(input("Quantity: "))

    toy_details = {
        "toy_name": toy_name,
        "toy_price": toy_price,
        "toy_quantity": toy_qty
    }

    toy_cart.append(toy_details)

# Calculate the total amount before applying discount and tax
total_amount = 0

print('\n---------------------------- Invoice Details ----------------------------')
print('Shop Name      : The Toy Store')
print(f'Customer Name  : {customer_name}\n')
print(f'{"Toy Name":<16}{"Price":<12}{"*":<3}{"Qty":<8}{"=":<3}{"Subtotal"}')
print('-' * 72)

# Loop through each toy in the cart and print line-wise billing
for toy in toy_cart:
    toy_sub_total = toy['toy_price'] * toy['toy_quantity']
    total_amount += toy_sub_total
    print(f"{toy['toy_name']:<16}{toy['toy_price']:<12.2f}* {toy['toy_quantity']:<7}= {toy_sub_total:.2f}")

# Apply discount based on total purchase amount
if total_amount < 5000:
    discount = 2
elif total_amount > 5000 and total_amount < 10000:
    discount = 5
elif total_amount > 10000:
    discount = 10
else:
    discount = 0

# Apply tax if applicable
if total_amount > 5000:
    product_tax = 2
else:
    product_tax = 0

# Calculate discount and tax amounts
discount_amount = (total_amount * discount) / 100
tax_amount = (total_amount * product_tax) / 100

# Final amount after discount and tax
discounted_total_amount = total_amount - discount_amount + tax_amount

# Print summary section
print('-' * 72)
print(f'{"Total Amount":<40}{total_amount:>20.2f}')
print(f'{"Discount Amount":<40}-₹{discount_amount:>19.2f}')
print(f'{"Tax Amount":<40}+₹{tax_amount:>19.2f}')
print('-' * 72)
print(f"\n{customer_name} spent a total of ₹{discounted_total_amount:.2f} after applying {discount}% discount.")

# Fixed price of each toy in INR
toy_price = 100

# Function to calculate and print customer's bill summary
def customer_bill_summary(customer_name, quantity, discount):
    # Calculate total amount before discount
    total_amount = quantity * toy_price

    # Calculate discount amount
    discount_amount = (total_amount * discount) / 100

    # Final payable amount after applying discount
    final_amount = total_amount - discount_amount

    # Display the summary
    print(f"Customer: {customer_name}")
    print(f"Total amount before discount: ₹{total_amount}")
    print(f"Discount applied ({discount}%): ₹{discount_amount}")
    print(f"Final amount to pay: ₹{final_amount}\n")

# Example function call
customer_bill_summary('Zahid', 50, 10)

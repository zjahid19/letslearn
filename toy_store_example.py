# Fixed price of each toy in INR
TOY_PRICE = 100

# Function to calculate detailed customer bill
def customer_bill_summary(customer_name, *quantities, **options):
    print(f"\n--- Bill Summary for {customer_name} ---")
    
    # Total number of toys
    total_toys = sum(quantities)
    
    # Base total amount
    total_amount = total_toys * TOY_PRICE
    
    # Discount handling
    discount = options.get("discount", 0)
    discount_amount = (total_amount * discount) / 100
    discounted_total = total_amount - discount_amount

    # Gift wrap fee (₹10 per toy)
    gift_wrap = options.get("gift_wrap", False)
    gift_wrap_charge = total_toys * 10 if gift_wrap else 0

    # Delivery charge
    delivery_charge = options.get("delivery_charge", 0)

    # Final total
    final_amount = discounted_total + gift_wrap_charge + delivery_charge

    # Display breakdown
    print(f"Total toys purchased: {total_toys}")
    print(f"Total before discount: ₹{total_amount}")
    print(f"Discount ({discount}%): ₹{discount_amount}")
    if gift_wrap:
        print(f"Gift wrap charges (₹10 per toy): ₹{gift_wrap_charge}")
    if delivery_charge:
        print(f"Delivery charge: ₹{delivery_charge}")
    print(f"Final amount to pay: ₹{final_amount}")

    return final_amount



customer_bill_summary(
    "Zahid",
    2, 4, 5,  # 3 toy types: total 11 toys
    discount=10,
    gift_wrap=True,
    delivery_charge=50
)

customer_bill_summary(
    "Ayesha",
    1, 2,
    discount=5
)

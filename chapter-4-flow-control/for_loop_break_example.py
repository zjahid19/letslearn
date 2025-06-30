# Correct PIN
correct_pin = "1234"

# Allow the user up to 3 attempts
for attempt in range(1, 4):
    user_input = input(f"Attempt {attempt}: Enter your 4-digit ATM PIN: ")
    
    if user_input == correct_pin:
        print("PIN accepted. Access granted.")
        break  # Exit the loop if PIN is correct
    else:
        print("Incorrect PIN.")
    
    # If it's the last attempt and still incorrect
    if attempt == 3:
        print("Too many incorrect attempts. Your card has been blocked.")
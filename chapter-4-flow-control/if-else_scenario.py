# Current fuel level in the car (measured in liters)
fuel_level = 15  

# Check if fuel level is below minimum threshold (10 liters)
if fuel_level < 10:
    # Action when fuel is low
    print('Let\'s refill the fuel first, then go to the office.')
else:
    # Action when fuel is sufficient
    print('Let\'s go to the office directly.')

# Program completion message
print('Program execution completed!')
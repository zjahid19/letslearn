# Initial fuel in the car (in arbitrary units)
fuel_in_car = 10

# Keep driving while there is enough fuel
while fuel_in_car > 1:
    print('INFO: Keep moving your car for the next 5 km...')
    fuel_in_car -= 1  # Reduce fuel by 1 unit after every 5 km

# This block runs when the fuel drops to 1 or less
else:
    print('WARNING: Your car is running out of fuel!')

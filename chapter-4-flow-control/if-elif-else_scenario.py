# Route availability
route_A = 'close'
route_B = 'open'
route_C = 'close'

# Starting the journey from home to office
print('Starting from home to reach office...')

# Check the available route in priority order: A > B > C
if route_A == 'open':
    print('Take a left turn through Route A and reach the office.')
elif route_B == 'open':
    print('Take a left turn through Route B and reach the office.')
elif route_C == 'open':  # Corrected this line: previously route_B was repeated
    print('Take a left turn through Route C and reach the office.')
else:
    print('All left routes are closed. Follow the straight route to reach the office.')

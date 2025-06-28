# Dictionary of all traffic breakers with their sizes
all_breaker_list = {'A': 'medium', 'B': 'medium', 'C': 'small', 'D': 'medium'}

# Start the journey
print('Starting the journey from home to office...\n')

# Loop through each breaker and check its size
for breaker, size in all_breaker_list.items():
    print(f"Reached speed breaker {breaker} (Size: {size}).")
    
    # If the breaker is too big, abort the journey
    if size == 'small':
        print("This speed breaker is too small. go ahead with normal speed.\n")
        continue
    
    # Otherwise, continue carefully
    print("Slow down your car and move forward carefully!\n")

# If the loop completes without breaking
else:
    print("Reached the office safely after crossing all speed breakers.")

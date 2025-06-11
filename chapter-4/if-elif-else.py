# Traffic Signal color when you reached at point D
current_light = "red"  # Can be "red", "yellow", or "green"

print(f"The traffic light is currently: {current_light}")

# Determine the appropriate action based on the light color
if current_light == "red":
    print("ACTION: Stop your vehicle completely.")
    
    
elif current_light == "yellow":
    print("ACTION: Slow down and prepare to stop.")
    
    
elif current_light == "green":
    print("ACTION: You may proceed if the intersection is clear.")
    
    
else:
    print("ALERT: Malfunctioning traffic light detected!")
    

print('Program execution completed !!')
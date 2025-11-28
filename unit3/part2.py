# Part 2: 24-Hour Clock Alarm Calculator

# Get the current time from the user
current_time = int(input("Enter the current time (in hours, 0-23): "))

# Get the number of hours to wait
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time using modulo operation
alarm_time = (current_time + hours_to_wait) % 24

# Display the result
print(f"\nThe alarm will go off at {alarm_time}:00 on the 24-hour clock.")


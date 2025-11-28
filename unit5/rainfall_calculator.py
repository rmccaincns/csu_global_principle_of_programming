"""
Part 1: Rainfall Calculator
This program uses nested loops to collect rainfall data over multiple years
and calculates the average rainfall per month.
"""

def main():
    # Ask for the number of years
    while True:
        try:
            num_years = int(input("Enter the number of years: "))
            if num_years <= 0:
                print("Please enter a positive number of years.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    total_months = 0
    total_rainfall = 0.0
    
    # Outer loop - iterate for each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        
        # Inner loop - iterate for each month (12 months)
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Enter the rainfall (in inches) for month {month}: "))
                    if rainfall < 0:
                        print("  Rainfall cannot be negative. Please try again.")
                        continue
                    break
                except ValueError:
                    print("  Invalid input. Please enter a valid number.")
            
            total_rainfall += rainfall
            total_months += 1
    
    # Calculate and display results
    print("\n" + "=" * 50)
    print("RAINFALL STATISTICS")
    print("=" * 50)
    print(f"Number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    
    if total_months > 0:
        average_rainfall = total_rainfall / total_months
        print(f"Average rainfall per month: {average_rainfall:.2f} inches")
    else:
        print("No data to calculate average.")
    print("=" * 50)


if __name__ == "__main__":
    main()


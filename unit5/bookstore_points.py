"""
Part 2: CSU Global Bookstore Points Calculator
This program calculates points awarded based on the number of books purchased.
"""

def calculate_points(books_purchased):
    """
    Calculate points based on the number of books purchased.
    
    Args:
        books_purchased: Number of books purchased
        
    Returns:
        Points awarded based on the purchase criteria
    """
    if books_purchased >= 8:
        return 60
    elif books_purchased >= 6:
        return 30
    elif books_purchased >= 4:
        return 15
    elif books_purchased >= 2:
        return 5
    else:
        return 0


def main():
    print("CSU Global Bookstore - Book Club Points")
    print("=" * 50)
    
    # Ask user for the number of books purchased
    while True:
        try:
            books = int(input("Enter the number of books purchased this month: "))
            if books < 0:
                print("Number of books cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Calculate points
    points = calculate_points(books)
    
    # Display results
    print("\n" + "-" * 50)
    print(f"Books purchased: {books}")
    print(f"Points awarded: {points}")
    print("-" * 50)


if __name__ == "__main__":
    main()


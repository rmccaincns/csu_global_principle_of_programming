class ItemToPurchase:
    """Class representing an item to purchase"""
    
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        """
        Default constructor
        Initializes item's name = "none", item's price = 0, item's quantity = 0
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        """
        Prints the item cost in the format:
        item_name quantity @ $price = $total
        """
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")


def main():
    """Main function to handle user input and calculate total cost"""
    
    # Item 1
    print("Item 1")
    print("Enter the item name:")
    name1 = input()
    print("Enter the item price:")
    price1 = float(input())
    print("Enter the item quantity:")
    quantity1 = int(input())
    
    # Create first ItemToPurchase object
    item1 = ItemToPurchase(name1, price1, quantity1)
    
    # Item 2
    print("\nItem 2")
    print("Enter the item name:")
    name2 = input()
    print("Enter the item price:")
    price2 = float(input())
    print("Enter the item quantity:")
    quantity2 = int(input())
    
    # Create second ItemToPurchase object
    item2 = ItemToPurchase(name2, price2, quantity2)
    
    # Calculate and display total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost:.0f}")


if __name__ == "__main__":
    main()


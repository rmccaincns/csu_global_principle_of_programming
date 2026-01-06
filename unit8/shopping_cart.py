# Online Shopping Cart Program
# CSU Global - Principles of Programming
# Portfolio Project


class ItemToPurchase:
    """Class representing an item to purchase."""
    
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        """
        Initialize an ItemToPurchase object with default or provided values.
        
        Args:
            item_name (str): Name of the item (default: "none")
            item_price (float): Price of the item (default: 0.0)
            item_quantity (int): Quantity of the item (default: 0)
            item_description (str): Description of the item (default: "none")
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        """Print the item name, quantity, price, and total cost."""
        total = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total)}")
    
    def get_item_cost(self):
        """Return the total cost for this item (quantity * price)."""
        return self.item_quantity * self.item_price


class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """
        Initialize a ShoppingCart object.
        
        Args:
            customer_name (str): Name of the customer (default: "none")
            current_date (str): Current date (default: "January 1, 2020")
        """
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        """
        Add an item to the cart.
        
        Args:
            item (ItemToPurchase): The item to add to the cart
        """
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        """
        Remove an item from the cart by name.
        
        Args:
            item_name (str): Name of the item to remove
        """
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_modify):
        """
        Modify an item's description, price, and/or quantity.
        
        Args:
            item_to_modify (ItemToPurchase): Item with new values to apply
        """
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                found = True
                # Only modify if the new values are not default values
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                break
        
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        """
        Get the total quantity of all items in the cart.
        
        Returns:
            int: Total quantity of all items
        """
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        """
        Calculate the total cost of all items in the cart.
        
        Returns:
            float: Total cost of all items
        """
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.get_item_cost()
        return total_cost
    
    def print_total(self):
        """Print the total cost of the shopping cart."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f"Total: ${int(self.get_cost_of_cart())}")
    
    def print_descriptions(self):
        """Print descriptions of all items in the cart."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    """
    Display the menu and handle user input.
    
    Args:
        cart (ShoppingCart): The shopping cart to manipulate
    """
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    
    valid_options = ['a', 'r', 'c', 'i', 'o', 'q']
    
    while True:
        print(menu)
        choice = input("Choose an option:\n")
        
        while choice not in valid_options:
            print("Invalid option. Please try again.")
            choice = input("Choose an option:\n")
        
        if choice == 'q':
            break
        elif choice == 'a':
            # Add item to cart
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            
            new_item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(new_item)
        
        elif choice == 'r':
            # Remove item from cart
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        
        elif choice == 'c':
            # Change item quantity
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            
            # Create a new ItemToPurchase with the name and new quantity
            modified_item = ItemToPurchase(item_name=name, item_quantity=quantity)
            cart.modify_item(modified_item)
        
        elif choice == 'i':
            # Output items' descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        
        elif choice == 'o':
            # Output shopping cart
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()


def main():
    """Main function to run the shopping cart program."""
    # Step 7: Prompt for customer name and date
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()
    
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    
    # Create shopping cart object
    cart = ShoppingCart(customer_name, current_date)
    
    # Run the menu
    print_menu(cart)


if __name__ == "__main__":
    main()


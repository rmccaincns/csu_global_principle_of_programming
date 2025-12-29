from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase


def print_menu(cart):
    """Print menu and process user choices
    
    Args:
        cart (ShoppingCart): The shopping cart to manipulate
    """
    menu = """MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:
"""
    
    choice = ""
    while choice != "q":
        print(menu)
        choice = input().strip().lower()
        
        if choice == "a":
            print()
            add_item_to_cart(cart)
        elif choice == "r":
            print()
            remove_item_from_cart(cart)
        elif choice == "c":
            print()
            change_item_quantity(cart)
        elif choice == "i":
            print()
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print()
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == "q":
            pass
        else:
            print("Invalid option. Please try again.")
        
        print()


def add_item_to_cart(cart):
    """Prompt user for item details and add to cart
    
    Args:
        cart (ShoppingCart): The shopping cart to add item to
    """
    print("ADD ITEM TO CART")
    item_name = input("Enter the item name:\n")
    item_description = input("Enter the item description:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    
    item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
    cart.add_item(item)


def remove_item_from_cart(cart):
    """Prompt user for item name and remove from cart
    
    Args:
        cart (ShoppingCart): The shopping cart to remove item from
    """
    print("REMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove:\n")
    cart.remove_item(item_name)


def change_item_quantity(cart):
    """Prompt user for item name and new quantity
    
    Args:
        cart (ShoppingCart): The shopping cart to modify
    """
    print("CHANGE ITEM QUANTITY")
    item_name = input("Enter the item name:\n")
    new_quantity = int(input("Enter the new quantity:\n"))
    
    # Create item with only name and quantity set (other fields default)
    modified_item = ItemToPurchase(item_name=item_name, item_quantity=new_quantity)
    cart.modify_item(modified_item)


def main():
    """Main function to run the shopping cart program"""
    # Get customer name and date
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()
    
    # Create shopping cart
    cart = ShoppingCart(customer_name, current_date)
    
    # Display menu
    print_menu(cart)


if __name__ == "__main__":
    main()


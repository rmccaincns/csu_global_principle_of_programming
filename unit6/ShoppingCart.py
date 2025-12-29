from ItemToPurchase import ItemToPurchase


class ShoppingCart:
    """Represents a shopping cart for a customer"""
    
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """Initialize shopping cart with customer name and date"""
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        """Adds an item to cart_items list
        
        Args:
            item (ItemToPurchase): The item to add to cart
        """
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        """Removes item from cart_items list
        
        Args:
            item_name (string): Name of the item to remove
        """
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_modify):
        """Modifies an item's description, price, and/or quantity
        
        Args:
            item_to_modify (ItemToPurchase): Item with new values
        """
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                # Only modify if the parameter has non-default values
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        """Returns quantity of all items in cart
        
        Returns:
            int: Total quantity of all items
        """
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        """Determines and returns the total cost of items in cart
        
        Returns:
            float: Total cost of all items
        """
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        """Outputs total of objects in cart"""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        
        print()
        print(f"Total: ${self.get_cost_of_cart():.0f}")
    
    def print_descriptions(self):
        """Outputs each item's description"""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


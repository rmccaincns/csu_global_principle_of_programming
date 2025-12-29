class ItemToPurchase:
    """Represents an item to purchase"""
    
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        """Initialize item with name, price, quantity, and description"""
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        """Print the item cost in format: name quantity @ $price = $total"""
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")
    
    def print_item_description(self):
        """Print item description in format: name: description"""
        print(f"{self.item_name}: {self.item_description}")


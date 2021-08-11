class Restaurant:
    """restaurant display message"""

    def __init__(self, name, cuisine):
        """initialize name and cuisine type attributes."""
        self.name = name
        self.cuisine = cuisine
        self.count = 0

    def open (self):
        """Display restaurant is open message."""
        print (f"{self.name} is now open! ")

    def closed (self):
        """Display restaurant is closed message after business hours."""
        print (f"{self.name} is currently closed. Please visit us during business hours! ")

    def customer_count (self, customers):
        """Count and display the number of customers served."""
        self.count += customers
        return self.count

my_restaurant = Restaurant ("Lauren's Dip N' Grill" , "Dips")
print (f"Welcome to {my_restaurant.name}. ")
print (f"Try our many {my_restaurant.cuisine}.")

my_restaurant.open()
my_restaurant.closed()
print (my_restaurant.customer_count(10))
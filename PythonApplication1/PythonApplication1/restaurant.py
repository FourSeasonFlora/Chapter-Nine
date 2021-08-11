#
#Chapter 9 Classes
#
#9-1
#restaurant
class Restaurant:
    """restaurant display message"""

    def __init__(self, name, cuisine):
        """initialize name and cuisine type attributes."""
        self.name = name
        self.cuisine = cuisine

    def open (self):
        """Display restaurant is open message."""
        print (f"{self.name} is now open! ")

    def closed (self):
        """Display restaurant is closed message after business hours."""
        print (f"{self.name} is currently closed. Please visit us during business hours! ")

my_restaurant = Restaurant ("Lauren's Dip N' Grill" , "Dips")
print (f"Welcome to {my_restaurant.name}. ")
print (f"Try our many {my_restaurant.cuisine}.")

my_restaurant.open()
my_restaurant.closed()
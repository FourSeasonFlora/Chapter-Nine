#
#9-3
#User profile example
#
class User:
    """Simple model of a user profile."""

    def __init__(self, first_name, last_name, age, state):
        """Initalize attributes of a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.state = state

    def describe_user (self):
        """prints a summary of the users info."""
        print (f"Age: {self.age} State: {self.state}")

    def greet_user (self):
        """greets the user."""
        print (f" Hello {self.first_name} {self.last_name}")

guest_profile = User ('Lauren', 'Acton', 29, 'MI')
guest_profile.describe_user ()
guest_profile.greet_user ()

admin_profile = User ('Administration', 'Only', 'N/A', 'N/A')
admin_profile.describe_user ()
admin_profile.greet_user ()

print (f"\nHello {guest_profile.first_name} {guest_profile.last_name}!")
print (f"\nWelcome {admin_profile.first_name}\n")
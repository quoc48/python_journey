class Restaurant:
    """A simple attempt to create a restaurant."""
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"\n--- Restaurant information ---")
        print(f"- Restaurant name: {self.name}")
        print(f"- Restaurant type: {self.type}")


    def open_restaurant(self):
        print(f"{self.name} restaurant is open!")

    def show_served(self):
        print(f"- Number of served customer: {self.number_served}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increase_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    """A simple attempt to present from parent class."""
    def __int__(self, name, type):
        super().__int__(name, type)

    def add_flavors(self, *flavors):
        self.flavors = flavors

    def show_flavors(self):
        print("\n--- IceCream flavors ---")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

my_restaurant = IceCreamStand('Ice Lovers', 'IceCreame Stand')
my_restaurant.describe_restaurant()

my_restaurant.add_flavors('apple', 'lime', 'chocolate')
my_restaurant.show_flavors()


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

my_restaurant = Restaurant('Little Cam', 'Coffee and Lunch')

my_restaurant.describe_restaurant()
my_restaurant.set_number_served(32)
my_restaurant.show_served()

my_restaurant.increase_number_served(2)
my_restaurant.show_served()




class Restaurant:
    """A simple attempt to create a restaurant."""
    def __init__(self, name, type):
        self.name = name
        self.type = type


    def describe_restaurant(self):
        print(f"{self.name}'s restaurant type is {self.type}.")


    def open_restaurant(self):
        print(f"{self.name} restaurant is open!")

first_restaurant = Restaurant('Little Cam', 'Coffee and Lunch')
second_restaurant = Restaurant('Topping Beef', 'Beef Steak')
third_restaurant = Restaurant('Domino','Pizza and Hambugar')
first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()




from restaurant import Restaurant, IceCreamStand as IC

first_restaurant = Restaurant('Pizza 4P', 'Luch and Dinner')
first_restaurant.describe_restaurant()

second_restaurant = IC('Lotte Ice Cream','Desert and Drinks')
second_restaurant.add_flavors('Lime','Apple','Mango')
second_restaurant.describe_restaurant()
second_restaurant.show_flavors()
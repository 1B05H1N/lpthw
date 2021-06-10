# there are 100 cars and/or the cars variable is a 100
cars=100
space_in_a_car=4
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study Drills
# Zed called 'car_pool_capacity' when he meant to call 'carpool_capacity'
# The interpreter (computer) didn't find the variable because it wasn't defined (didn't exist)
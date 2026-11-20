orders_list = ['tea','chai','paneer_rool','samosa','egg_puff','curry_puff']
for order in orders_list:
    print(order)


# • Real Life: You have a physical list of 4 passengers. You call out each name one at a time and mark them "Present."
# • Python List: passengers = ["Aarav", "Priya", "Rohan", "Ananya"]

passengers_list = ["Aarav", "Priya", "Rohan", "Ananya"]

for passenger in passengers_list:
    print(f"Passenger name :{passenger} and check whether the seat is checked ?!: {input('status: ')}")
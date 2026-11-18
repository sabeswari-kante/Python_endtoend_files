# A tea stall offers different prices for different cup sizes.
# Write a program that caculates the price based on size
# Task
# - Input: 'small', 'medium','large'
# - small: -->$ 10, Medium-->$15,, Large-->$20
# - If invalid: show "unknown cup size"



user_order = input('''whats the type of coffe you would like to order; Here is the menu: \nBlack coffee, \ndoppio,\nTurkish coffe, \nFrench press, \ncold brew, \nnitro cold brew,
                   \nMasala chai, \nAdrak chai, \nTulasi chai::Your order 😊:: ''').lower() 


items_dictionary = {
                    'coffee': {'black coffee':20,'doppio':25,'turkish coffee':15, 'french press':30,'cold brew':10, 'nitro cold brew':15},
                    'chai':{'masala chai':10,'adrak chai':15,'tulasi chai':15} 
                    }
size_prices= {'small':1, 'medium':15,'large':20}


for category, type in items_dictionary.items():
    if user_order in type:
        size_cup= input('the size of the cup please; is it medium, small, or large?!: ').strip().lower()
        basic_amount = type[user_order]
        size_price_of_order = size_prices.get(size_cup)
        the_total_amount = basic_amount+ size_price_of_order +0.18*basic_amount
        print(f"The bill amount of your order with gst applied is : {the_total_amount}")
        break
else:
    print("unknown order! the order is not avaliable...😑😑")
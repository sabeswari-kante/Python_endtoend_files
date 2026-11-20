
# you're creatng a tea menu board
# each item must be numbered.
# Task:
# - use enumerate() to print menu items with numbers

orders_list = ['tea','chai','paneer_rool','samosa','egg_puff','curry_puff']
# print(list(enumerate(orders_list)))
# print(list(enumerate(orders_list, start = 1)))

for idx, item in enumerate(orders_list,start = 1):
    print(f'{idx}:{item} ')
    # print(idx,item)

# youre preparing an order summary with customer with customer names and their bill amount
# Task:
# use two lists:
# one for names and one for bills
# print: '[name] paid $[amount]'

customer_names = ['sita','rama','lakshman','lakshmi','vishnu','gowri','shiva']
bill_amount_of_customers = [40,20,63,95,40,85,52]

# the output of zip is tuples

for customer_and_bill_amount in zip(customer_names,bill_amount_of_customers):
    print(customer_and_bill_amount)

for customer, bill_amount in zip(customer_names,bill_amount_of_customers):
    print(f'Customer name : {customer} and bill maount is {bill_amount}')

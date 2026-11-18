# A local cafe wants a program that suggests a snack
# If acustomer asks for cookies or samosa, it confirms the order.Otherwise, it says it's not avaliable

# Task:
# - take snack input if its 'cookies' or 'samosa', confirm the customer_order
# - else, show unavailability 

# code

customer_order = input('Order please?!: ').strip().upper()
if customer_order =='SAMOSA' or customer_order=='COOKIES':
    print(f'Thankyou for your order, you will receive your order within 5 minutes')
else:
    print('Unavailability')
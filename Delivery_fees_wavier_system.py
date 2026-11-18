# You run an online tea store.
# If the order amount is more than $300, , delivery is free;
# otherwise, it costs $30

# Task:
# -input : order_amount
# -use ternary operator to decide delivery Fee

order_amount= int(input('Enter the order amount here: '))
delivery_fee = 0
if order_amount<300:
    delivery_fee= 30
    print(f'The final order_amount: ${order_amount+delivery_fee}')
    print('$30 delivery charges apply')
else:
    print(f'order_amount: ${order_amount}')
    print('Zero delivery charges apply')


overall_order_amount = 0+order_amount if order_amount>300 else 30+order_amount


# task 
# generate a multiplication table 

table = int(input('Enter the table number: ').strip())
count=1
for iteration in range(1,11):
    print(f"{table} * {count} = {table*count}")
    if count <=10:
        count +=1
    else:
        break
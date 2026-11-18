# You're creating a notifications system for a smart kettle
# It should remind the user only when the kettle has finished boling task:
# - A varaible kettle_boiled = True
# - If boiled, show "kettle done! Time to make chai"



# code 

# taking user input
 
kettle_temp= input('Does the kettle has finished boling task, reply Y or N: ').strip().upper()
kettle_boiled = True if kettle_temp == 'Y' else False

if kettle_boiled :
    print("kettle done! Time to make chai")
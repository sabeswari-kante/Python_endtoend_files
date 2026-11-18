# You're building a ticket info system for a railway app.'
# 'Based on seat type, show its features'
# ''
# 'Task:'
# '- Input: 'sleeper','AC','general', 'luxury'
# - Match using match_case
# - Unknown ->show: "invalis seat type"


# seat_type_user_input = input("Enter the seat type; ac/sleeper/general/luxury: ").strip().lower()

# match seat_type_user_input:
#     case 'sleeper':
#         print('Sleeper- No AC, beds avaliable')
#     case 'ac':
#         print('The cost is bit higher compared to sleeper and bedsheets are also aloted based on train ')
#     case 'general':
#         print('the cheapest ago all the avaliable options and no reservation but no beds and absence of ac')
#     case 'luxury':
#         print('Luxury - Premium seats with meals ')
#     case _:
#         print('Invalid user input')

########### Python 3.10 introduced a new way to hand;e multiple user roles like 'admin', 'editor' or 'viewer'--- That is : match-case

command = 'play_music'

match command:
    case 'play_music':
        print('launch spotify ')
    case 'turnoff lights':
        print('turning off lights')
    
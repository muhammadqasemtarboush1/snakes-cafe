#  the menu of the titles in the restaurant
menu = [
    {
        'title': 'Appetizers',
        'subtitle': [
            'Wings',
            'Cookies',
            'Spring Rolls'
        ]
    },
    {
        'title': 'Entrees',
        'subtitle': [
            'Salmon',
            'Steak',
            'Meat Tornado',
            'A Literal Garden'
        ]
    },
    {
        'title': 'Desserts',
        'subtitle': [
            'Ice Cream',
            'Cake',
            'Pie'
        ]
    },
    {
        'title': 'Drinks',
        'subtitle': [
            'Coffee',
            'Tea',
            'Unicorn Tears'
        ]
    }
]

print(
    '**************************************\n**  Welcome to the Snakes Cafe!   **\n**  Please see our menu below.  **\n** To quit at any time, type "quit" **\n**************************************')


def get_menu():
    for x in menu:
        print(x['title'])
        print('---------')
        for y in x['subtitle']:
            print(y)
        print('\n')


get_menu()

all_dishes = ''
for z in menu:
    for j in z['subtitle']:
        all_dishes += j.lower() + ' '

print('***********************************')
user_order = input(' What would you like to order?  ').lower()

def make_order(user_input):
    counter = 1
    orders = ''
    finish_order = False
    for x in menu:
        for y in x['subtitle']:
            if y.lower() == user_input:

                orders += user_input + ' '
                print(f'{counter} order of {orders} have been added to your meal')
                exit_msg = input('type quit to finish or No to complete your order : ')
                finish_order = True

                while exit_msg != 'quit':
                    user_order = ''
                    if y.lower() == user_input:

                        user_order = input(' What would you like to order?  ').lower()
                        if user_order in all_dishes:
                            counter += 1
                            orders += user_order + ' '
                            print(f'{counter} order of {orders} added')
                            exit_msg = input('type quit to finish or No  to complete your order : ')
                            finish_order = True
                        else:
                            print('invalid input, select again ')
                            finish_order = False

    if finish_order:
        print(f'your order {orders} has been submitted :)  :')
    else:
        print(f'Please check our menu what you asked for isn"t available into our restaurant:')


make_order(user_order)
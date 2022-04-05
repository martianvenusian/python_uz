from ast import FormattedValue
from numpy import full_like


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


'''
while True:
    print('\nPlease tell me your name:')
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''

while True:
    print('\nPlease tell me your name:')
    f_name = input("First name: ")
    if f_name.lower() == 'palonchi':
        break
    l_name = input("Last name: ")
    if l_name == 'Pustonchi':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

def build_person_dic(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


akbar = build_person_dic('Akbar', 'Subhonberdiyev')
husan = build_person_dic('Husan', 'Vohidov')

print(akbar)
print(husan)


def build_item_dic(name, price='', color=''):
    item = {'name': name, 'price': price, 'color': color}
    return item


name = 'apple'
price = 5000
color = 'green'

item_dic = build_item_dic(name, price, color)
print(item_dic)

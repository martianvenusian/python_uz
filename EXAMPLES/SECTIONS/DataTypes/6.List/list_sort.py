# numbers
ages = [27, 28, 18, 19]
print(ages)
# [27, 28, 18, 19]

ages.sort()
print(ages)
# [18, 19, 27, 28]

numbers = [27, 178.0, 80.0]
numbers.sort()
print(numbers)
# [27, 80.0, 178.0]

# litters
names = ['akbar', 'akrom', 'huoyiddin', 'dilmurod']
print(names)
# ['akbar', 'akrom', 'huoyiddin', 'dilmurod']

names.sort()
print(names)
# ['akbar', 'akrom', 'dilmurod', 'huoyiddin']

names = ['akbar', 'Subxonberdiyes', 'Kamzayev',  'akrom']
print(names)
# ['akbar', 'Subxonberdiyes', 'Kamzayev', 'akrom']


names.sort()
print(names)
# ['Kamzayev', 'Subxonberdiyes', 'akbar', 'akrom']


mixed = ['akrom', 27, 80.0, 178.0]
print(mixed)
# mixed.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'

# reverse argument
ages = [27, 28, 18, 19]
ages.sort(reverse=True)
print(ages)
# [28, 27, 19, 18]

ages = [27, 28, 18, 19]
ages.sort(reverse=False)
print(ages)
# [18, 19, 27, 28]

ages = [27, 28, 18, 19]
ages.sort()
print(ages)
# [18, 19, 27, 28]

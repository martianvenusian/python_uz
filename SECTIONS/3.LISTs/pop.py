# .pop()
names = ['akrom', 'dilmurod', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

deleted_name = names.pop()
print(names)
# ['akrom', 'dilmurod', 'akbar']


names = ['akrom', 'dilmurod', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

deleted_name = names.pop(1)
print(names)
['akrom', 'akbar', 'humoyiddin']
print(deleted_name)
# dilmurod


deleted_name = names.pop(0)
print(names)
['akbar', 'humoyiddin']
print(deleted_name)
# akrom

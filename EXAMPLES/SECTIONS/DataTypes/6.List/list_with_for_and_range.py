names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']

for i in range(1, 3):
    print(names[i])

# akrom
# humoyiddin

names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']

start_index = 0
last_index = len(names)

for i in range(start_index, last_index):
    print(names[i])
# akbar
# akrom
# humoyiddin
# dilmurod
# elmurod

names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']

for i in range(0, len(names)):
    print(names[i])
# akbar
# akrom
# humoyiddin
# dilmurod
# elmurod

names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']

for i in range(0, len(names)):
    print('name', i + 1, ":", names[i])

# name 1 : akbar
# name 2 : akrom
# name 3 : humoyiddin
# name 4 : dilmurod
# name 5 : elmurod

names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod']

for i in range(0, len(names)):
    names[i] = 'name' + str(i)

print(names)
# ['name0', 'name1', 'name2', 'name3']

names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod']

for i in range(0, len(names)):
    names[i] = i

print(names)
# [0, 1, 2, 3]

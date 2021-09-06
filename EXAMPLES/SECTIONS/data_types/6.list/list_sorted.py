names = ['akrom', 'akbar', 'humoyiddin']

sorted_names = sorted(names)

print(names)
# ['akrom', 'akbar', 'humoyiddin']

print(sorted_names)
# ['akbar', 'akrom', 'humoyiddin']

# reverse argument
ages = [27, 28, 18, 19]
sorted_ages = sorted(ages, reverse=True)
print(sorted_ages)
# [28, 27, 19, 18]


sorted_ages = sorted(ages, reverse=False)
print(sorted_ages)
# [18, 19, 27, 28]


sorted_ages = sorted(ages)
print(sorted_ages)
# [18, 19, 27, 28]

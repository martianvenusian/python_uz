numbers = list(range(1, 10, 3))
print(numbers)
# [1, 4, 7]

# max()
print('max: ', max(numbers))
# max:  7

# min()
print('min: ', min(numbers))
# min:  1

# sum()
print('sum:', sum(numbers))
# sum: 12


ages = [27, 28, 18, 19]

# max()
max_num = max(ages)
print(max_num)
# 28

# min()
min_num = min(ages)
print(min_num)
# 18


# sum()
sum_num = sum(ages)
print(sum_num)
# 92


names = ['akbar', 'humoyiddin', 'akrom']

print(min(names))
# akbar

print(max(names))
# humoyiddin

print(sum(names))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


names = ['akbar', 'humoyiddin', 'akrom', 'Hamzayev']

# max()
max_name = max(names)
print(max_name)
# humoyiddin

# min()
min_name = min(names)
print(min_name)
# Hamzayev

# sum()
sum_names = sum(names)
print(sum_names)
# Traceback (most recent call last):
#   File "<string>", line 12, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

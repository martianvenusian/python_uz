numbers = list(range(1, 10, 3))
print(numbers)
# [1, 4, 7]

print('max: ', max(numbers))
# max:  7

print('min: ', min(numbers))
# min:  1

print('sum:', sum(numbers))
# sum: 12

names = ['akbar', 'humoyiddin', 'akrom']

print(min(names))
# akbar

print(max(names))
# humoyiddin

print(sum(names))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

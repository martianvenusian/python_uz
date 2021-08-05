### `min()`, `max()` va `sum()` funksiyalari va list

Sonlardan iborat bo'lgan listning eng kichik, eng katta, va sonlarining yig'indisini quyidagicha hisoblash mumkin:

```python
numbers = list(range(1, 10, 3))
print(numbers)
# [1, 4, 7]

print('max: ', max(numbers))
# max:  7

print('min: ', min(numbers))
# min:  1

print('sum:', sum(numbers))
# sum: 12
```

Qiymatlari so'zlardan iborat bo'lgan listing eng kichik va eng katta qiymatini ham hisoblash mumkin:

```python
names = ['akbar', 'humoyiddin', 'akrom']

print(min(names))
# akbar

print(max(names))
# humoyiddin
```

Lekin elementlarining turi string bo'lgan listning elementlarining yig'indisini hisoblashda xatolikni kelib chiqishi mumkin:

```python
names = ['akbar', 'humoyiddin', 'akrom']
print(sum(names))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

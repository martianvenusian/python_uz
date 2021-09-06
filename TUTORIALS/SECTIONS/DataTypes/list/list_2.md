### `.sort()` funksiyasi yordamida listni tartiblash

```python
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
```

```python
# litters
names = ['akbar', 'akrom', 'huoyiddin', 'dilmurod']
print(names)
# ['akbar', 'akrom', 'huoyiddin', 'dilmurod']

names.sort()
print(names)
# ['akbar', 'akrom', 'dilmurod', 'huoyiddin']

names = ['akbar', 'Subxonberdiyev', 'Kamzayev',  'akrom']
print(names)
# ['akbar', 'Subxonberdiyes', 'Kamzayev', 'akrom']

names.sort()
print(names)
# ['Kamzayev', 'Subxonberdiyes', 'akbar', 'akrom']

```

```python
mixed = ['akrom', 27, 80.0, 178.0]
print(mixed)
# mixed.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
```

### `sorted()` funksiyasi yordamida listni tartiblash

```python
names = ['akrom', 'akbar', 'humoyiddin']

sorted_names = sorted(names)

print(names)
# ['akrom', 'akbar', 'humoyiddin']

print(sorted_names)
# ['akbar', 'akrom', 'humoyiddin']
```

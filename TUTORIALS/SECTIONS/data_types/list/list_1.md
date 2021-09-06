`List` bu o'zida ko'plab ma'lumotlarni saqlovchi python tiling ma'lumot tur(_data type_)idan biri.

### Listni yaratish.

List turt burchak egizak (`[]`) qavslar yordamida yaratiladi:

```python
list = []
print(list)
# []
```

Ishonch hosil qilish uchun yaratilgan listning turini quydagicha teksherib ko'rishimiz mumkin:

```python
list = []
print(type(list))
# <class 'list'>
```

List elementlari bilan birga yaratilishi mumkin. Qavslar orasida listning elementlari joylashadi. Listning har bir elementi vergul yordamida ajratiladi.

```python
names = ['Akrom', 'Akbar', 'Humoyiddin']
print(names)
#['Akrom', 'Akbar', 'Humoyiddin']
```

Listning elementlari turli ma'lumot turlariga tegishli bo'lishi mumkin.

```python
ages = [27, 17, 24]
print(ages)
# [27, 17, 24]
```

```python
weights = [82.1, 75.5, 65.0]
print(weights)
# [82.1, 75.5, 65.0]
```

```python
height = [175.2, 175.5, 170.0]
print(height)
# [175.2, 175.5, 170.0]
```

```python
marriage_statues = [True, False, False]
print(marriage_statues)
# [True, False, False]
```

Bir vaqtning o'zida listning elementlarining turlari turlicha bo'lishi ham mumkin.

```python
student_info = ['Akbar', 17, 75.5, 175.5, False]
print(student_info)
# ['Akbar', 17, 75.5, 175.5, False]
```

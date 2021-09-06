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

Listning elementlari turli ma'lumot turlariga tegishli bo'lishi mumkin. Shu jumladan harflar, so'zlar, 0-9 gacha raqamlar yoki istalgan sonlar.

```python
names = ['Akrom', 'Akbar', 'Humoyiddin']
print(names)
#['Akrom', 'Akbar', 'Humoyiddin']
```

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

### Listni elementlari murojaat.

Listning elementlariga murojaat uning indeks raqamini ko'rsatish orgali amalga oshirish mumkin.
Listining _indeks raqami 1dan emas 0dan_ boshlanadi. Ya'ni birinchi elementning indeks raqami 0.

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[0])
# Akrom
```

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[1])
# Akbar
```

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[2])
# Humoyiddin
```

Mavjud bo'lmagan indeks raqami orqali elementga murojaat qilish xatolikka olib keladi.

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[3])
# IndexError: list index out of range
```

Listning elementlariga murojaatni manfiy indekslar yordamida ham amalga oshiriladi.
Bunda listning elementlariga murojaat chapdan o'nga emeas, aksincha o'ngdan chapga qarab murojaat qilinadi.
Manfiy indeks -0 dan emas aksincha -1 dan boshlanadi. Chunki -0 indeks 0 indeksni anglatadi.

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[-0])
# akrom
```

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[-1])
# humoyiddin
```

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[-2])
# akbar
```

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[-3])
# akrom
```

Mavjud bo'lmagan manfiy indeks orqali elementga murojaat qilish ham o'z navbatida xatolikka olib keladi.

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names[-4])
# IndexError: list index out of range
```

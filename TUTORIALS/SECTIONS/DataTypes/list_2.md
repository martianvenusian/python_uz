### `for` takrorlovchi opertor yordamida listning elementlarini chop qilish

Aytaylik sizda ismlarni o'zida saqlovchi list mavjud. Va siz bu listning har bir elementini chop qilmoqchisiz. Bu ishni **_for_** takrorlovchi operatori yordamida amalga oshirsangiz bo'ladi.

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod']

for name in names:
    print(name.title())

# Akbar
# Akrom
# Humoyiddin
# Dilmurod
```

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod']

for name in names:
    print("Student's name is ", name.title())

# Student's name is  Akbar
# Student's name is  Akrom
# Student's name is  Humoyiddin
# Student's name is  Dilmurod
```

Huddi shu ishni sonlar bilan ham amalga oshirishingiz mumkin.

```python
ages = [19, 27, 24, 28]

for age in ages:
    print(age)
# 19
# 27
# 24
# 28
```

```python
ages = [19, 27, 24, 28]

for age in ages:
    print("Student's age is ", age)
# Student's age is 19
# Student's age is 27
# Student's age is 24
# Student's age is 28
```

### `for` takrorlovchi operatori va `range()` funksiyasi yordamida listning elementlari ustida ishlash

**_for_** operatori **_range()_** funksiyasi yordamida listning elementlariga birma bir murojat qilish mumkin. Bunda **_range()_** funksiyasi yordamida listning qaysi elementidan qaysi elementigacha murojat qilishni belgilab olishingiz kerak bo'ladi. Misol uchun 1chi elementdan 3chi elementgacha listning elementlarini chop qilib ko'raylik. Buni quydagicha alamga oshirsa bo'ladi.

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']

for i in range(1, 3):
    print(names[i])
# akrom
# humoyiddin
```

Agar listning barcha elementlarini chop qilmoqchi bo'lsangiz unda buni quydagicha amalga oshirsangiz bo'ladi.

```python
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
```

Yuqoridagi misolni boshqacharoq ko'rinishda amalga oshirishingiz mumkin.

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']

for i in range(0, len(names)):
    print(names[i])
# akbar
# akrom
# humoyiddin
# dilmurod
# elmurod
```

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']
for i in range(0, len(names)):
    print('name', i + 1, ":", names[i])

# name 1 : akbar
# name 2 : akrom
# name 3 : humoyiddin
# name 4 : dilmurod
# name 5 : elmurod
```

**_for_** operatori **_range()_** funksiyasi yordamida listning elementlarining qiymatini yangi boshqa qiymatga o'zgartirishingiz mumkin.

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod']

for i in range(0, len(names)):
    names[i] = 'name' + str(i)

print(names)
# ['name0', 'name1', 'name2', 'name3']
```

```python
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod']

for i in range(0, len(names)):
    names[i] = i

print(names)
# [0, 1, 2, 3]
```

### `range()` funksiyasi yordamida list hosil qilish

Aytaylik siz malum bir qonuniyatga asoslanga yoki qandaydir ketma-ketlikka ega bo'lgan sonlarni o'zida saqlovchi list yaratmoqchisiz. Bu ishni **range()** funksiyasi yordamida qilsangiz bo'ladi. Bu ayniqsa juda ulkan sonlarni o'zida saqlovchi listni yaratishda juda ham qulaydir.

0dan 9gacha bo'lgan sonlarni o'zida saqlovchi listni quydagicha yaratamiz:

```python
numbers = list(range(0, 10))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Toq sonlar ketma-ketligi quydagicha yaratiladi:

```python
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)
# [1, 3, 5, 7, 9]
```

Juft sonlar ketma-ketligi esa quydagicha yaratiladi:

```python
even_numbers = list(range(2, 10, 2))
print(even_numbers)
# [2, 4, 6, 8]
```

Qiymati 3ga o'sib boruvchi sonlar ketma ketligi esa quydagicha yaratiladi:

```python
three_step_numbers = list(range(1, 10, 3))
print(three_step_numbers)
# [1, 4, 7]
```

10 qiymatga oshib boruvchi 0dan 100gacha bo'lgan sonlar ketma-ketligini quydagicha yaratamiz

```python
ten_step_numbers = list(range(0, 101, 10))
print(ten_step_numbers)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

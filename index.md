## List

#### Listga oxiriga element qo'shish

Agar siz listga element qo'shmoqchi bo'lsangiz `.appent()` metodidan foydalanishingiz mumkin. Bu metod listning oxiridan boshlab listga element qo'shadi.

```python
names = ['akrom']
print(names)
# ['akrom']

names.append('akbar')
print(names)
# ['akrom', 'akbar']

names.append('humoyiddin')
print(names)
# ['akrom', 'akbar', 'humoyiddin']
```

#### Listga element kiritish

Agar siz listga biror bir element kiritmoqchi bo'lsangiz `.insert()` metodidan foydalaning. Bu metod listning istalgan qismiga yangi element qo'shadi. Faqat bunda kiritilayotgan yangi elementning o'rnini ko'rsatish lozim.

```python
names = ['akrom', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'akbar', 'humoyiddin']

names.insert(1, 'dilmurod')
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

names.insert(3, 'elmurod')
print(names)
# ['akrom', 'dilmurod', 'akbar', 'elmurod', 'humoyiddin']
```

#### `del` ifodasi yordamida listdan elementni o'chirib tashlash

Agar o'chirmoqchi bo'layotgan elementingizning joylashgan o'rnini bilsangiz `del` ifodasi yordamida bu ishni amalga oshirishingiz mumkin

```python
names = ['akrom', 'dilmurod', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

del names[2]
print(names)
# ['akrom', 'dilmurod', 'humoyiddin']

del names[0]
print(names)
# ['dilmurod', 'humoyiddin']
```

#### `.pop()` metodi yordamida listdan elementni o'chirib tashlash

Siz listdan elementni o'chirib tashlamoqchisiz lekin o'chirilgan elementni biror bir o'zgaruvchiga o'zlashtirib olmoqchi bo'lsangiz `.pop()` metodidan foydalanishizgiz mumkin. Bu metod listning oxirgi elementini o'chiradi va o'chirilgan elementning qiymatini qaytaradi.

```python
names = ['akrom', 'dilmurod', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

deleted_name = names.pop()
print(names)
# ['akrom', 'dilmurod', 'akbar']
```

Agar listning faqat oxirgi elementini emas balki istalgan biror bir elementini o'chirmqochi bo'lsangiz unda .pop() metodiga o'chirmoqchi bo'layotgan elementning o'rnini ko'rsatish kerak bo'ladi.

```python
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
```

#### `.remove()` metodi yordamida listdan elementni o'chirib tashlash

Agar siz elementning joylashgan o'rnini bilmasangiz unda elementning qiymati yordamida listdan elementning o'chirishingiz mumkin. Buning uchun `.remove()` metodidan foydalaning.

```python
names = ['akrom', 'dilmurod', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

names.remove('akbar')
print(names)
# ['akrom', 'dilmurod', 'humoyiddin']

names.remove('akrom')
print(names)
# ['dilmurod', 'humoyiddin']
```

## Boolean ifodalar

`True` va `False` (rost va yolg'on) ifodalari

```python
print(True)
# True
```

```python
print(False)
# False
```

```python
condition = True
print(condition)
# True
```

```python
condition = False
print(condition)
# False
```

## Shart ifodalari

#### Tenglik sharti

```python
name = 'akrom'
print(name == 'Akrom')
# False
```

```python
name = 'akrom'
print(name.title() == 'Akrom')
# True
```

```python
age = 27
print(age == 27)
# True
```

```python
age = 27
print(age == 72)
# False
```

#### Teng emaslik sharti

```python
name = 'akrom'
print(name != 'Akrom')
# True
```

```python
name = 'akrom'
print(name.title() != 'Akrom')
# False
```

```python
age = 27
print(age != 27)
# False
```

```python
age = 27
print(age != 72)
# True
```

#### Katta yoki kichik shartlari

```python
age = 19
print(age < 21)
# True
```

```python
age = 19
print(age > 21)
# False
```

#### Katta va teng shartlari

```python
age = 19
print(age >=21)
# False
```

```python
age = 21
print(age >= 21)
# True
```

```python
age = 22
print(age >= 21)
# True
```

#### Kichik va teng shartlari

```python
age = 22
print(age <= 21)
# False
```

```python
age = 21
print(age <= 21)
# True
```

```python
age = 20
print(age >= 21)
# True
```

#### `and` shart yordamchi so'zi

```python
age = 27
name = 'akrom'

print(age == 27 and name.title() == 'Akrom')
# True
```

```python
age = 27
name = 'akrom'

print(age == 27 and name == 'Akrom')
# False
```

#### `or` shart yordamchi so'zi

```python
age = 27
name = 'akrom'

print(age == 27 or name.title() == 'Akrom')
# True
```

```python
age = 27
name = 'akrom'

print(age == 27 or name.title() == 'Akbar')
# True
```

```python
age = 27
name = 'akrom'

print(age == 28 or name.title() == 'Akbar')
# False
```

#### Shartlarni qavslar bilan yozish

```python
age = 27
name = 'akrom'

condition = (age == 27 and name.title() == 'Akrom') or (age == 19 and name.title() == 'Akbar')
print(condition)
# True
```

```python
age = 19
name = 'akbar'

condition = (age == 27 and name.title() == 'Akrom') or (age == 19 and name.title() == 'Akbar')
print(condition)
# True
```

```python
age = 19
name = 'akrom'

condition = (age == 27 and name.title() == 'Akrom') or (age == 19 and name.title() == 'Akbar')
print(condition)
# False
```

<!--
## if shart amali

Dasturlashda holarni biror bir shart asosida tekshirish va shu tekshiruv asosida keyingi qaysi amallarni bajarishni belgilab olish odatiy holatdir. Python dasturlash tilida bu amal `if` shart amali yordamida amalga oshiriladi.

#### misol 1 (String)

#### misol 1 (String)

```python
boy_or_girl = 'boy'

if boy_or_girl == 'boy':
    print('He is a', boy_or_girl)
else:
    print('She is a', boy_or_girl)
```

#### misol 2
-->
<!--
## Funksiyalar

Funksiya bu ma'lum bir vazifani bajaruvchi va o'z nomiga ega bo'lgan maxsus blokka olingan kodga aytiladi. Funksiya yordamida dasturda tez-tez takrorlanuvchi bir xil vazifani bajaruvchi kodlarni qayta-qayta yozishning oldini olish mumkin. Yani biror vazifani bajaruvchi kod yozishga to'g'ri kelganda shu vazifani bajaruvchi funksiyani chaqirish kifoya. Buning uchun dasturning biror qismida funksiya yaratiladi va shu funksiyaga ihtiyoj tug'ilganda uni chaqirib bajarilishi kerak bo'lgan vazifa unga yuklanadi.
-->
<!--
#### Funksiyani yaratish

Python dasturlash tilida funksiya `def` maxsus so'zi yordamida ifodalanadi. _def_ maxsus so'zi funksiya yaratilayotganligini ifodalaydi va _def_ dan so'ng `funksiyaning nomi` beriladi. Funksiyaning nomidan so'ng `()`(qavs) ochib yopiladi va `:`(ikki nuqta) qo'yish orqali funksiyani ifodalash yakunlanadi. Ikki nuqtadan keyingi kodning blok qismi funksiyaning `tana`si hisoblanadi va qachonki funksiyaga murojat qilinganda funksiya tanasi ishga tushadi. Funksiya yaratilish davomida qavslar bo'sh bolishi mumkin (quyidagi 1-misol kabi), yoki funksiyaning qavslari o'z ichiga biror bilan ma'lumotni ham olishi mumkin (quyidagi 2-misol kabi). Bu haqida qiyingi qismlarda to'liqroq ma'lumot beriladi.

```python
def func():
    w = "Bu shunchaki oddiy funksiya."
    print(w)
```

```python
def func(w):
    print(w)
```

#### Funksiyaga murojaat qilish

Yaratilgan funksiyaga muroajaat shu funksiyaning nomi va qavslarni yozish orqali amalga oshiriladi.

```python
func()
>>> Bu shunchaki oddiy funksiya
```

Yuqorida funksiyani chaqirdik va chaqirilgan funksiya o'z tanasini ishga tushirish orqali _\'Bu shunchaki oddiy funksiya.\'_ degan gapni chop etdi.

Qavslar orasida ma'lumot qabul qiluvchi funksiyaga esa quydagicha murojaat qilinadi.

```python
word = "Bu shunchaki oddiy funksiya."
func(word)
>>> Bu shunchaki oddiy funksiya.
```

Funksiya qavslari orasidagi _word_ o'zgaruvchisi orqali qiymat qabul qilda va shu qiymatni o'z tanasida qayta ishlab _\'Bu shunchaki oddiy funksiya.\'_ deb chop qildi. _\'word\'_ o'zgaruvchisiga biror bir qiymatni berish orqali istagan boshqa so'zni funksiyaga uzatishimiz va shu so'zni fuksiya yordamida chop qilishimiz mumkin.

```python
word = "Bu endi shunchaki oddiy funksiya emas."
func(word)
>>> Bu endi shunchaki oddiy funksiya emas.
```

-->

<!-- ## Kitoblar tarjimasi

1. [Python Crash Course](https://martianvenusian.github.io/python-crash-course/)

2. Python Cookbook -->

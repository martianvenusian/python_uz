### `.appent()` metodi yordamida listga element qo'shish

Agar siz listga element qo'shmoqchi bo'lsangiz **.appent()** metodidan foydalanishingiz mumkin. Bu metod listning oxiridan boshlab element qo'shadi.

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

### `.insert()` metodi yordamida listga element kiritish

Agar siz listga biror bir element kiritmoqchi bo'lsangiz **.insert()** metodidan foydalaning. Bu metod listning istalgan qismiga yangi element qo'shadi. Faqat bunda kiritilayotgan yangi elementning o'rnini ko'rsatish lozim.

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

### `del` ifodasi yordamida listdan elementni o'chirish

Agar o'chirmoqchi bo'layotgan elementingizning joylashgan o'rnini bilsangiz **del** ifodasi yordamida bu elementni o'chirib tashlashingiz mumkin

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

### `.pop()` metodi yordamida listdan elementni o'chirish

Siz listdan elementni o'chirib tashlamoqchisiz lekin o'chirilgan elementni biror bir o'zgaruvchiga o'zlashtirib olmoqchi bo'lsangiz **.pop()** metodidan foydalanishizgiz mumkin. Bu metod listning oxirgi elementini o'chiradi va o'chirilgan elementning qiymatini qaytaradi.

```python
names = ['akrom', 'dilmurod', 'akbar', 'humoyiddin']
print(names)
# ['akrom', 'dilmurod', 'akbar', 'humoyiddin']

deleted_name = names.pop()
print(names)
# ['akrom', 'dilmurod', 'akbar']
print(deleted_name)
# akbar
```

Agar listning faqat oxirgi elementini emas balki istalgan biror bir elementini o'chirmoqchi bo'lsangiz unda **.pop()** metodiga o'chirmoqchi bo'layotgan elementning o'rnini ko'rsatish kerak bo'ladi.

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

### `.remove()` metodi yordamida listdan elementni o'chirish

Agar siz elementning joylashgan o'rnini bilmasangiz unda elementning qiymati yordamida listdan elementni o'chirishingiz mumkin. Buning uchun **.remove()** metodidan foydalaning.

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

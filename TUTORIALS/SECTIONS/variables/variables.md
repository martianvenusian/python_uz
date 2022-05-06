### O'zgaruvchi nima?

O'zgaruvchi (`variable`) bu ma'lum bir ma'lumot turi(`data type`)ga mansub bo'lgan va biror bir qiymatga ega bo'lgan ma'lumotni saqlash uchun kompyuter xotirasida ajratilgan joyga aytiladi. Boshqacha qilib aytganda, python dasturida o'zgaruvchi ma'lumotlarni qayta ishlash uchun ma'lumotning qiymati va turiga qarab kompyuter xotirasidan ma'lum bir kattalikda joy ajratadi va bu ma'lumotlarni o'sha joyda saqlaydi. Dastur ishlash davomida bu ajratilgan joylarda saqlanayotgan o'zgaruvchining qiymati o'zgarishi mumkin. Umuman olganda o'zgaruvchini ma'lumotlaringizni saqlaydigan maxsus quti deb tushinsangiz bo'ladi. Va bu qutini nima bilan to'ldirish yoki umuman bo'sh saqlash bu sizning qo'lingizda.

O'zgaruvchi o'z **_nomi_**(`name`) va **_qiymat_**(`value`)iga ega bo'ladi. O'zgaruvchilarni nomlash qonun-qoidalari va ularni qiymatlari to'g'risida birozdan keyin to'liq ma'lumotga ega bo'lasiz.

Python dasturlash tilida xar bir o'zgaruvchi ma'lum tur(`data type`)ga ega bo'ladi. Bu ma'lumot turlari `Integer`, `String`, `Float`, `List`, `Tuple`, `String`, `Dictionary` va hakozo ma'lumot turlari bo'lishi mumkin. O'zgaruvchining ma'lumot turi huddi yuqoridagi misol kabi quti nima bilan to'ldirilganiga qarab uning qanaqa turdagi quti ekanligi ma'lum bo'ladi. Agar qutini olma bilan to'ldirsangiz demak bu quti o'zida olmani saqlovchi qutiga aylanadi. Agar qutini olmadan bo'shatib suv bilan to'ldirsangiz o'zida suv saqlovchi qutiga aylanadi. Ma'lumot turlari haqida keyingi darslarda bilib olasiz.

### O'zgaruvchini e'lon qilish

O'zgaruvchilarni e'lon qilish uning nomi va qiymatini belgilash orqali amalga oshiriladi

```python
number = 100
print(number)
# 100
```

Bu yerda biz bir o'zgaruvchi yaratdek. Bu o'zgaruvchimizning nomini **_number_** deb nomladek va uning qiymatini **_100_** soni qilib belgiladek. **_print_** funksiyasi yordamida o'zgaruvchimizni chop qilib tekshirib ko'ramiz va natijada uning qiymati **_100_**ga teng ekaniga ishonch hosil qilamiz. Bu o'zgaruvchimizning qiymati butun songa teglashtirganimiz uchun uning ma'lumot tur(`data type`)i `integer` bo'ladi. Bu haqda keyingi darslarda bilib olasiz.

```python
name = 'Akbar'
print(name)
# Akbar
```

Bu yerda biz **_Akbar_** degan ismni o'zida saqlovchi o'zgaruvchi yaratdek. Bu o'zgaruvchimizning nomini **_name_** deb belgiladek va uning qiymatini **_Akbar_** ismiga yani xarf va belgilardan iborat bo'lgan so'zga tenglashtirdek. **_print_** funksiyasi yordamida o'zgaruvchimizni chop qilib ko'ramiz va uning qiymati **_Akbar_**ga teng ekaniga ishonch hosil qilamiz. Bu o'zgaruvchimizning qiymati xarf va belgilardan tuzilgan so'zga teglashtirganimiz sababli uning ma'lumot turi `string` bo'ladi. Bu haqda keyingi darslarda bilib olasiz.

### O'zgaruvchilarni nomlash

O'zgaruvchilarni nomlash python dasturlash tilining ma'lum qonun-qoidalariga asosan amalga oshiriladi. Bu qoidalarga amal qilmaslik dasturda xatolik(`error`)larga olib keladi.

- o'zgaruvching nomi faqat harflardan iborat bo'lishi mumkin:

```python
age = 20
name = 'Akbar'
```

- o'zgaruvching nomi harflar va raqamlar birlashmasidan iborat bo'lishi mumkin:

```python
age1 = 20
name1 = 'Akbar'
```

- o'zgaruvching nomi harflar, raqamlar va pastki chiziqcha(**_undescore_**) dan iborat bo'lishi mumkin:

```python
age_1 = 20
name_1 = 'Akbar'
```

- o'zgaruvchining nomi harf yoki pastki chizicha bilan boshlanishi mumkin:

```python
age_1 = 20
_name = 'Akbar'
```

- Biroq o'zgaruvching nomi raqam bilan boshlanishi mumkin emas:

```python
1_age = 20 # mumkin emas
```

- O'zgaruvchini nomi paski chiziqcha bilan ajratib yozilishi mumkin lekin bo'sh joy (**_space_**) ajratib yozilishi mumkin emas:

```python
student_name = 'Akbar' # mumkin
student name = 'Akbar' # mumin emas
```

- O'zgaruvchlarni nomlashda pastki chiziqchdan boshqa maxsus belgilarni ishlatish mumkin emas:

```python
a-g-e = 20
*age = 20
age* = 20
age_* = 20
```

- O'zgaruvchilarni nomlashda Python dasturlash tilining tarkibida bo'lgan maxsus so'zlaridan foydalanish mumkin emas:

```python
import = 'Akbar'  # mumkin emas
pass = 'Akbar' # mumkin emas
continue = 'Akbar' # mumkin emas
break = 'Akbar' # mumkin emas
```

### O'zgaruvchilarni nomlashda va ulardan foydalanganda muhim holatlar:

- O'zgaruvchilarni nomlashda biror ma'noga ega bo'lgan qisqa so'zlardan foydalangan yaxshiroq. Bu dasturinggizni siz va boshqa dasturchilarga tushinarliroq qiladi. Misol uchun o'zda biror bir ismni saqlaydigan o'zgaruvchining nomini **_n_** deb nomlagandan ko'ra **_name_** deb nomlagan ancha tushinarliroq bo'ladi.

```python
n = 'Akbar'
name = 'Akbar' #
```

- O'zgaruvchilarni nomlagandan keyin undan foydalanishda o'zgaruvching nomidagi kichik bir harf yoki belgining tushib qolishi yoki boshqa harf yoki belgi bilan almashtirib yozib yuborish dasturda xatolik yoki dasturning notug'ri ishlashiga olib kelishi mumkin:

```python
name = 'Akbar'
print(Name)
# NameError: name 'Name' is not defined
```

```python
numbers = 100
print(number)
# NameError: name 'number' is not defined
```

### O'zgaruvchining qiymatini o'zgartirish yoki o'zgaruvchini qayta e'lon qilish

```python
number = 100
print(number)
# 100

number = 10
print(number)
```

Yuqorida **_number_** degan o'zgaruvchi yaratdek va uning qiymatini 100 soni deb belgiladek. Va keyinchalik uning qiymatini 10 soniga o'zgartirdek.

Agar o'zgaruvchining qiymatini o'zgaruvchi ega bo'lgan bir xil ma'lumot to'riga o'zgartirsak unda faqat o'zgaruvchining qiymatini o'zgartirgan bo'lamiz. Yani yuqorida **_100_** sonini **_10_**ga o'zgartirganimizdeb. Bunda o'zgaruvchining ma'lumot turi o'zgarmaydi.

```python
number = 100
print(number)
# 100

number = 'hundred'
print(number)
# numdred
```

Yuqorida **_number_** degan o'zgaruvchi yaratdek va uning qiymatini **_100_** soni deb belgiladek. Va keyinchalik uning qiymatini **_hundred_** so'ziga almashtirish orqali o'zgaruvchini qayta e'lon qildek (yaratdek). Bunda o'zgaruvching qiymatini **_100_** sonidan **_hundred_** so'ziga o'zgartirdek. Bunda o'zgaruvching qiymati bilan birga uning ma'lumot tur(`data type`)i ham o'zgaradi. Bu jarayonda o'zgaruvchini qayta e'lon qildek deb tushinsak bo'ladi.

- O'zgaruvchini qayta e'lon qilish yoki qiymatini o'zgartirish ma'lum ma'noda bir biriga o'xshash amal yoki jarayon deb tushinsak ham bo'ladi.

### O'zgaruvchini o'chirish

`del` buyrug'i yordamida o'zgaruvchini o'chirish mumkin

```python
name = 'Akbar'
print(name)
# Akbar

del name
print(name)
# in <module>
#    print(name)
# NameError: name 'name' is not defined
```

Yuqorida **_name_** degan o'zgaruvchi yaratdek. Uni qiymatini **_print_** buyrug'i yordami chop qilib ko'rdek.
**_del_** del buyrug'i yordamida bu o'zgaruvchini o'chirdek va yana bir bor **_print_** buyrug'i yordamida tekshirib ko'rganimizda bu **_name_** deb nomlangan o'zgaruvchi yaratilmagani haqidagi xotolik xabar(**_NameError_**)ini oldek.

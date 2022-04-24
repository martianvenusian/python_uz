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
## Funksiyalar
Funksiya bu ma'lum bir vazifani bajaruvchi va o'z nomiga ega bo'lgan maxsus blokka olingan kodga aytiladi. Funksiya yordamida dasturda tez-tez takrorlanuvchi bir xil fazifani bajaruvchi kodlarni qayta-qayta yozishning oldini olish mumkin. Yani biror vazifani bajaruvchi kod yozishga to'g'ri kelganda shu vazifani bajaruvchi funksiyani chaqirish kifoya. Buning uchun dasturning biror qismida funksiya yaratiladi va shu funksiyaga ihtiyoj tug'ilganda uni chaqirib bajarilishi kerak bo'lgan vazifa unga yuklanadi.

### Funksiyani yaratish
```python
def func():
    """Bu funksiya shunchaki matnni chop qiladi"""
    word = "Bu shunchaki oddiy funksiya"
    print(word)
```
### Funksiyani chaqirish

```python
func()
>>> body of the function
```
### Funksiyaga ma'lumotlarni berish
```python
def func(word):
    """Bu funksiya shunchaki matnni chop qiladi"""    
    print(word)

word = "Bu shunchaki oddiy funksiya"
func(word)
>>> Bu shunchaki oddiy funksiya
```
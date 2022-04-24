# Shart ifodalari

### Tenglik sharti

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

### Teng emaslik sharti

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

### Kattalik sharti
```python
age = 19
print(age > 21)
# False
```

```python
age = 22
print(age > 21)
# True
```

### Kichiklik sharti

```python
age = 19
print(age < 21)
# True
```
```python
age = 22
print(age < 21)
# False
```

### Katta va tenglik sharti

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

### Kichik va tenglik sharti

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
print(age <= 21)
# True
```

### `and` shart yordamchi so'zi

```python
condition1 = True
condition2 = True

print(condition1 and condition2)
# True
```

```python
condition1 = True
condition2 = False

print(condition1 and condition2)
# False
```

```python
condition1 = False
condition2 = True

print(condition1 and condition2)
# False
```

```python
condition1 = False
condition2 = False

print(condition1 and condition2)
# False
```

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

### `or` shart yordamchi so'zi

```python
condition1 = True
condition2 = True

print(condition1 or condition2)
# True
```

```python
condition1 = True
condition2 = False

print(condition1 or condition2)
# True
```

```python
condition1 = False
condition2 = True

print(condition1 or condition2)
# True
```

```python
condition1 = False
condition2 = False

print(condition1 or condition2)
# False
```

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

### Shartlarni qavslar bilan yozish

```python
age = 27
condition = (age == 27) or (age == 19)
print(condition)
# True
```

```python
name = 'akrom'
condition = (name.title() == 'Akrom') and (name.title() == 'Akbar')
print(condition)
# False
```

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
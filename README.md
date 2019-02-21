https://classroom.github.com/a/ZpdKtloc

# Üçüncü Seminarın Tapşırıqları

**1. n sayda elementdən ibarət olan bir ölçülü matrisin ən böyük elementini tapan proqram yazın.**

```python
matrix = [2, 45, 2, 12, 34]

# Sizin kodunuz .....

max = 45
```

**2. n sayda elementdən ibarət olan matrisin ən böyük və ən kiçik elementlərinin cəmini tapın.**
```python
matrix = [2, 45, 2, 12, 34]

# Sizin kodunuz .....

sum_of_min_max = 47 # max = 45 min = 2 ona görə min + max = 47
```

**3. String dəyişənlərdən ibarət matrisdə uzunluğu 2-dən çox olan elementləri tapın**

```python
matris = ['al', 'kitab', 'film', 'yol', 'stul']

# Sizin kodunuz .....

output = ['kitab', 'film', 'yol', 'stul']
```

**4. Elementləri tuple olan list(matris) verilib. Listi tuple-ların sonuncu elementlərinin artması sırası ilə düzün.**

```python
matris = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

# Sizin kodunuz .....
# nəticə
matris = [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

```

**5. s string dəyişəni verilib. Elə yeni string dəyişəni düzəldin ki, bu dəyişən original s stringinin ilk 2 və son 2 simvolundan ibarət olsun. Əgər s dəyişənin uzunluğu 2-dən kiçik olarsa yeni string dəyişən boş olsun**

```python
s = "spring" # original 

y = "spng" # yeni

s = "apple" # original

y = "appe" #yeni

```

**6. Matrisi transformasiya edən program yazın**

İstifadə olunan python bilikləri:
 - list
 - loop
# Nümunə:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```
**7. Fikrimdə tutulan ədədin tapılması. Tutaq ki, fikrimdə 1 və 99 arasında bir ədəd tutmuşam. Sizin həmin ədədi tapmaq üçün `n` şansınız var**

İstifadə olunan python bilikləri
 - random
 - for
 - if

# Nümunə:
```python
import random
n = int(input("Maksimal təxmin etmə şansını daxil edin"))
number = random.randint(1, 99)

# proqramın ardını siz tamamlayın...
```

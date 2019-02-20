**Bu sayt pythonda printi format etmək üçündür:**
```python
https://pyformat.info/
```

```python
a = ["bir", "iki", "üç", "dörd", "beş", "altı", "yeddi", "səkkiz", "doqquz"]

b = ["on", "iyirmi", "otuz", "qırx", "əlli", "altmış", "yetmiş", "səksən", "doxsan"]

n = int(input("ədəd daxil edin: "))



spell = ""

while n != 0:
        q = n % 10 # 4
        n = n // 10 # 0
        if n != 0:
                spell = a[q - 1] + spell # beş
        else:
                spell = b[q - 1] + " " + spell

print(spell)


# n = 234

'''

234 

q = 234 % 10 -> 4
n = 234 / 10 -> 23


q = 23 % 10 -> 3
n = 23 / 10 -> 2

q = 2 % 10 -> 2
n = 0



'''


n = int(input("ededi daxil edin: "))


# sum = 0

# while n != 0:
# 	q = n % 10
# 	print(q)
# 	sum = sum + q
# 	n = n // 10 
# 	print(n)
# 	print('------')

# print(sum)


total = 0

products = ["alma", "armud", "gilas"]

product_prices = [1.2, 2.3, 2.8]

basket = [2, 1, 1]

num = 0

#(2, 3) tuple

for i in basket:
	total = total + i * product_prices[num]
	print("{0} kq {1}: {2} AZN".format(i, products[num], i * product_prices[num]))
	num = num + 1

print("Ümumi məbləğ: %0.2f" % total)



matris = []
n = 5
s = 0
while n > 0:
	# eded daxil edin
	num = int(input("daxil edin: "))
	#kvadratini tap
	num = num * num
	# her defe tapilan kvadrati cemle
	s = s + num
	# kavdarti matrise elave et
	matris.append(num)
	#saygaci azalt
	n = n - 1


print(matris)

```

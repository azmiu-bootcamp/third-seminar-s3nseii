#matirse daxil olan en boyuk  ve en kicik ededin cemi 
n = 5

matrix = []


while n != 0:

    num = int(input('Matrise daxil etmek istediyiniz ededleri girin: '))

    matrix.append(num)

    n -= 1
print(matrix)

print ("max qiymeti:",max(matrix))

print ("min qiymeti:",min(matrix))
#cem
print("max ve min cemi:",min(matrix) + max(matrix) )

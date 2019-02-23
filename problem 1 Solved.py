#max value of matrix
n = 5
end = 0
matrix = []


while n != 0:

    n = int(input('Matrise daxil etmek istediyiniz ededleri girin: '))

    matrix.append(n)

#this is just warning
    
    if len(matrix) > 3:
        
        print ('bitirmek istediyiniz zaman 0 daxil edin')
       
print(matrix)
print (max(matrix))

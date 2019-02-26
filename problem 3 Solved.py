list = ['al', 'kitab', 'film', 'yol', 'stul']

for word in list[:]:
  if len(word) <=2:
    list.remove(word) 
    print (list)

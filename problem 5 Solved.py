s = input('Her hansi bir soz daxil edin: ')
print (s)

if len(s) <=2:
  y = (".......")
  print (y)
else:
  y = s[0]+s[1] + s[-1] +s[-2]
  print (y)

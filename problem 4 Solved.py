def getKey(item):
  return item[0]
matris = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
matris.sort(key=getKey)
print (matris)

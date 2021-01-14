def total (a=5, *numbs, **pbook):
    print ("a", a)
    for i in numbs:
        print ('element', i)
    for x, z in pbook.items():
        print (x,z)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

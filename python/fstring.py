first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))

nod = first if first<second else second
print (nod)
while first % nod != 0 or second % nod != 0:
#while first%nod==0 and second%nod==0:
    nod -=1
print (nod)
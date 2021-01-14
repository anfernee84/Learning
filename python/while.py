a = input ('Enter a digit ')
while type (a) != int:
    try:
        a = int(a)
    except ValueError:
        print ('Enter correct digit')
        a = input ('Enter a digit ')
if a % 2 == 0:
    print ('4etnoe')
else:
    print ('Ne4etnoe')

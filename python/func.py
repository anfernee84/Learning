#def countfood():
#    a = int(input())
#    b = int(input())
#    print ('Total' , a+b, 'food' )
#
#print ('How much food ate monkeys?') 
#countfood()
#
#print ('How much food ate dogs?')
#countfood()
#
#print ('How much food ate mice?')
#countfood()
def pryamougolnik():
    a = float(input("Width :"))
    b = float (input('Height :'))
    print ("ploshad ravna : %.2f" % (a*b) )
def triangle():
    a = float (input ('Osnova :'))
    h = float (input ('Vysota'))
    print ("ploshad ravna : %.2f" % (0.5*a*h))
def circle():
    r = float (input ('Radius :'))
    print ('Ploshad ravna : %.2f' % (3.14*(r**2)))

figure = input('Enter number of figure: 1 - pryamougolnik, 2 - treugolnik, 3 - kgug:  ')
if figure == '1':
    pryamougolnik()
elif figure =='2':
    triangle()
elif figure =='3':
    circle()
else:
    print('WTF?')
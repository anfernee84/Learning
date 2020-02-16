x = float(input('Enter first digit '))
y = float(input('Enter second digit '))
op = input ('Select the operation (-),(+),(*),(/) ')
if op == '+':
    print(x,'+',y,'=',x+y)
elif op == '-':
    print(x,'-',y,'=',x-y)
elif op == '*':
    print(x,'*',y,'=',x*y)
elif op == '/':
    if y == 0: 
        print('You cannot divide by zero')
    else:
        print(x,'/',y,'=',x/y)
else:
    print ('Check data')
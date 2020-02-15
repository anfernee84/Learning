num = int(input('Enter digit: '))
if num == 1000:
    print('OMG\n') 
if num >0 or num == -5:
    if num == -5:
        print ('your number is -5')
    elif num>0 and num<10:
        print('number is more than zero and less than 10')
    elif num>10 and num<20:
        print('number is more than 10 and less than 20')
    elif num >20 and num <30:
        print('number is more than 20 and less than 30')
    elif  num >30:
        print('number is more than 30')
else:
    print ('WTF?')
print('All is ok!') 
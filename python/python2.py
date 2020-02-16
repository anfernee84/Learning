num = input('Enter digit: ')
if  num == '':
    print ('You forgot to enter a digit')
elif int (num) == 1000:
    print('OMG\n') 
elif int (num) >0 or int (num) == -5:
    if int (num) == -5:
        print ('your number is -5')
    elif int (num)>10 and int (num)<20:
        print('number is more than 10 and less than 20')
    elif int (num) >20 and int (num) <30:
        print('number is more than 20 and less than 30')
    elif  int (num) >30:
        print('number is more than 30')
    else:
        print('number is more than zero and less than 10')
else:
    print ('WTF?')
print('All is ok!') 


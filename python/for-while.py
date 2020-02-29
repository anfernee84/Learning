i = 1000
while i > 100:
    print(i)
    i /= 2

for j in 'hello world':
    if j == 'a':
        break
    print(j * 2, end = '' )
else:
    print('There`s no letter "a" ')
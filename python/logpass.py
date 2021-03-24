a = input ("Enter a digit: ")
while True:
    try:
        a = int(a)
    except ValueError or TypeError:
        print(f"is not a digit {a}")
        a = input ("Enter a digit: ")
    else:
        a = int(a)
        break
#    print (a)
if a % 2 == 0:
    print (f"{a} is even")
else:
    print (f'{a} is odd')
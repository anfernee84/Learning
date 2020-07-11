def bitcoin_to_usd(btc, curs):
    amount = btc * curs
    print(amount)
    
bitcoin_to_usd(round(4,6), 9150)

def mult (x,y):
    equals = x * y
    print (equals)
mult(float(input("x = ")), float(input("y = ")))

def sum (x,y):
    plus = x + y
    print (plus)
sum (float(input("x = ")), float(input("y = ")))

def div (x,y):
    delenie = x / y
    if x > y:
        print (delenie)
    else:
        print ("WTF?")
div (float(input("x = ")), float(input("y = ")))

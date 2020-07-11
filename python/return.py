def res (x,y):
    znak = str(input("Enter symbol: "))
    if znak == "*":
        return x*y
    elif znak == "+":
        return x+y
    elif znak == "-":
        return x-y
    elif znak == "/":
        if x>=y:
            return x/y
        else:
            return "WTF?"

print(res(int(input("x = ")), int(input("y = "))))




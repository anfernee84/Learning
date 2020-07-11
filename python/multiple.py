def function():
    a = int(input())
    b = a
    while a != 0:
        a = int(input())
        if a == 0:
            break
        b *= a 
    return b
 
print(function())
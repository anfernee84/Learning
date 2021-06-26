from random import randint

def get_random_password():
    s = "()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    random_pass = ""
    symbol = ""
    count = 0
    while count < 8:
        symbol = randint(0, len(s)-1)
        random_pass += s[symbol]
        count +=1
    print(type(random_pass))    
    return(random_pass)
print(get_random_password())
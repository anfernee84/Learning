def is_valid_password(password):
    up = 0
    lo = 0
    di = 0
    if len(password) < 8:
        return False
    else:
        for i in password:
            if i.islower():
                lo+=1
            elif i.isupper():
                up+=1
            elif i.isdigit():
                di+=1
    if up > 0 and lo > 0 and di > 0:
        return True
    else:
        return False
            
print(is_valid_password("!R2w3e4r"))
def is_integer(s):
    
    if s == ' ':
        return False
    if len(s) == 0:
        return False
    elif len(s) > 0:
        s = s.replace(' ', '')
        s = s.removeprefix("-")
        s = s.removeprefix("+")
        for i in s:
            try:
                i == int(i)
            except:
                return False
        return True
        

        
print (is_integer(' '))    


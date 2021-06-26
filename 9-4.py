def is_valid_pin_codes(pin_codes):
    codes = []
    if pin_codes == []:
        return False
    for i in pin_codes:
        print(i)
        if i.isdigit() and i == str(i) and i not in codes and i != "" and len(i) == 4:
            codes.append(i)
            print(codes)        
        else:
            return False    
    return True   


print(is_valid_pin_codes(['1101', '9034', '0011']))
print(is_valid_pin_codes([]))